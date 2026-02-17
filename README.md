# fits-test-cases

A curated collection of FITS files for regression testing FITS I/O libraries. Each file has a companion `.md` document describing its structure, provenance, and the FITS features it exercises.

## Directory Layout

| Directory | Files | Source | Description |
|---|---|---|---|
| `nasa-samples/` | 15 | [NASA GSFC FITS samples](https://fits.gsfc.nasa.gov/fits_samples.html) | Reference files from HST, EUVE, Astro-1, and other NASA missions. Covers image extensions, binary/ASCII tables, random groups, and tile-compressed images. |
| `hipsgen/` | 10 | [CDS hipsgen-cat](https://github.com/cds-astro/cds-hipsgen-cat) | HEALPix tiles at various orders from the CDS HiPS tile generator. All single-HDU binary tables with identical schemas. |
| `rust-fitsio/` | 7 | [rust-fitsio](https://github.com/simonrw/rust-fitsio) | Test fixtures from the Rust `fitsio` crate. Includes boolean columns, hypercubes, unsigned short images, and multi-extension files. |
| `fitsio-pure-fixtures/` | 6 | [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure) | Test fixtures from this project's parent library. NICMOS mosaics, IUE spectra, WFPC2 associations, compressed images, and binary tables. |
| `cfitsio/` | 5 | [HEASARC cfitsio](https://github.com/HEASARC/cfitsio) | Iterator test files from the canonical C FITS library. Binary tables and images used for column/row/image iteration tests. |
| `vizier/` | 4 | [CDS VizieR](https://vizier.cds.unistra.fr/) | Catalog query results from VizieR. Includes Gaia DR3 transits, NVSS radio cutouts, and variable star light curves. |
| `hips/` | 2 | [CDS hips2fits](https://alasky.cds.unistra.fr/hips-image-services/hips2fits) | HiPS cutout service outputs. Large multi-extension HST/PHAT mosaic and a Pan-STARRS allsky tile. |
| `misc/` | 2 | Various | Miscellaneous files: Bonn 1420 MHz survey and a SkyView cutout. |
| `astrometry/` | 1 | [astrometry.net](https://astrometry.net/) | Astrometric solution correspondence table from the astrometry.net solver. |

## FITS Features Covered

- Primary HDU images (8/16/32/64-bit integer, 32/64-bit float)
- Image extensions (multiple per file)
- Binary table extensions
- ASCII table extensions
- Random groups format (deprecated, used in UVFITS)
- Tile-compressed images (Rice algorithm)
- Boolean columns
- Multi-dimensional arrays (3D cubes, 4D+ hypercubes)
- Unsigned integer images via BZERO
- HEALPix tables
- Multi-extension files (up to 15+ HDUs)

## Usage

Each `.fits` or `.fit` file has a corresponding `.md` file with the same basename. The markdown file documents:

- **Provenance**: Where the file came from and what instrument/survey produced it
- **HDU structure**: Number and types of HDUs, dimensions, data types
- **FITS features**: Which aspects of the FITS standard the file exercises
- **File size**: On-disk size

## Contributing

To add a new test file:

1. Place it in the appropriate directory (or create a new one)
2. Add a companion `.md` file documenting the file's structure and provenance
3. Keep files under 50MB where possible

## License

Test files are redistributed for testing purposes. Individual files retain their original licenses and usage terms from their respective sources.
