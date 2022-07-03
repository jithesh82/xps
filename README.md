# xps
A python code to process and fit x-ray photoelectron spectra (XPS).

## Usage
To choose data region and background substract:

`python3 preparedata.py testdata.xlsx`

To fit:

`python3 processdataandfit.py testdata.xlsx testguess.xlsx`

The testdata.xlsx is the excel xps data file.  The first two columns are respectively binding energy and intensity.  The spectra is assumed to be background substracted and corrected for any charging.

The testguess.xlsx contains the guess values for the peaks.  The first three columns are respectively intensity, binding energy and peak width (fwhm).

## Screenshots
Selecting data region and background substraction:
![alt text](https://github.com/jithesh82/xps/blob/main/selectbgsub.png)
Fitting:
![alt text](https://github.com/jithesh82/xps/blob/main/fitexample.png)

## References
Test data:  Mendeley xps data.  
