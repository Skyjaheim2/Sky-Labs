# Sky-Labs

Sky Labs is a flask application inspired by https://www.symbolab.com/ that allows users to do mathematical computations.

![ss6](https://user-images.githubusercontent.com/64718777/160222532-f7a5cdac-4a5f-493b-beb1-9ce4152479e7.png)
![ss7](https://user-images.githubusercontent.com/64718777/160222561-184628a2-5317-4769-8824-1a72ec96c9d0.png)
![ss10](https://user-images.githubusercontent.com/64718777/160222573-67394226-9da5-428d-bc60-e41604a62cc2.png)

## Requirements

All requirements are listed in requirements.txt.

## Features

* Arithmetic operations
* Algebraic operations: Add/Subtract/Multiply exponentials, radicals and fractions.
* View history of computations.
* Live solve: Do operations in real time. 

## Technologies

* Python Flask
* Vanilla JavaScript

## Testing

Unit tests for the backend are located in the 'Testing' folder and were written using the unittest library.
````
python -m unittest test_Methods.py
````

## Usage
Visit https://sky-labs.herokuapp.com/ or execute `` flask run application.py `` to run locally.

As of now, only operations done under the 'Algebra' tab are functional.

### Keywords
Keywords such as 'simplify' or 'combine' can be used before an expression to perform specific operations.
As of now, only two keywords are supported: 'simplify' and 'combine' for fractions.
![image](https://user-images.githubusercontent.com/64718777/160222426-e78cda86-eb72-4b59-a002-0915c613eabc.png)


## Contributors

* https://github.com/Skyjaheim2

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)