# xps
A python code to fit background substracted x-ray photoelectron spectra (XPS).

## Usage
`python3 fitxps.py testdata.xlsx testguess.xlsx`

The testdata.xlsx is the excel xps data file.  The first two columns are respectively binding energy and intensity.  The spectra is assumed to be background substracted and corrected for any charging.

The testguess.xlsx contains the guess values for the peaks.  The first three columns are respectively intensity, binding energy and peak width (fwhm).

## Screenshots
![alt text](https://github.com/jithesh82/cocktail_recipes/blob/main/fitexample.png)

## References
Test data:  Mendeley xps data.  
