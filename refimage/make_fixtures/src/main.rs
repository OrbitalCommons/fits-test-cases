//! Write the refimage 1.0.0-pre6 fixtures in this directory:
//! `cargo run --release -- <output dir>`.
use refimage::{
    ColorSpace, DynamicImageOwned, FitsCompression, FitsWrite, GenericImageOwned, Gzip, Hcompress,
    ImageOwned, PixelStor, Quantize, Rice,
};
use std::time::Duration;

fn img<T: PixelStor>(data: Vec<T>, w: usize, h: usize) -> GenericImageOwned
where
    DynamicImageOwned: From<ImageOwned<T>>,
{
    let ts = chrono::DateTime::from_timestamp(1_700_000_000, 0).unwrap();
    let image = ImageOwned::from_owned(data, w, h, ColorSpace::Gray).unwrap();
    let mut g = GenericImageOwned::new(ts, Duration::from_millis(1500), DynamicImageOwned::from(image));
    g.insert_key("CAMERA", "Test Cam").unwrap();
    g
}

fn main() {
    let out = std::env::args().nth(1).expect("output directory");
    let (w, h) = (57usize, 23usize);
    let u16d: Vec<u16> = (0..w * h).map(|i| (i as u16).wrapping_mul(977)).collect();
    let f32d: Vec<f32> = (0..w * h)
        .map(|i| 100.0 + 10.0 * ((i as f32) * 0.37).sin() + (i % 7) as f32)
        .collect();
    let cases: Vec<(&str, GenericImageOwned, FitsCompression)> = vec![
        ("u16_none", img(u16d.clone(), w, h), FitsCompression::NONE),
        ("u16_gzip", img(u16d.clone(), w, h), Gzip::new().into()),
        ("u16_rice", img(u16d.clone(), w, h), Rice::new().into()),
        ("u16_rice_tile16x8", img(u16d.clone(), w, h), Rice::new().tile_dims([16, 8]).into()),
        ("u16_hcompress", img(u16d.clone(), w, h), Hcompress::new().into()),
        ("f32_none", img(f32d.clone(), w, h), FitsCompression::NONE),
        ("f32_gzip", img(f32d.clone(), w, h), Gzip::new().into()),
        ("f32_rice_dither", img(f32d.clone(), w, h), Rice::new().quantize(Quantize::new()).into()),
        ("f32_hcompress", img(f32d, w, h), Hcompress::new().quantize(Quantize::new()).into()),
    ];
    for (name, g, c) in cases {
        std::fs::write(format!("{out}/{name}.fits"), g.fits_bytes(c).unwrap()).unwrap();
    }
}
