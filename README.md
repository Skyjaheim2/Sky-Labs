# Sky-Labs

Sky Labs is a computer algebra system (CAS) inspired by https://www.symbolab.com/ that allows users to do symbolic mathematical computations.

![image](https://user-images.githubusercontent.com/64718777/160222769-b98b45a5-01c8-416d-b0a3-b2ac1212238c.png)
![image](https://user-images.githubusercontent.com/64718777/178858974-76149a69-eb5b-41f4-9c5e-f70e59b79c0c.png)
![image](https://user-images.githubusercontent.com/64718777/178869284-b5129fa4-69c7-42fd-b41f-0985c996e211.png)
![image](https://user-images.githubusercontent.com/64718777/160734861-a7e43995-607c-4a57-a440-f7800f3cf887.png)
![image](https://user-images.githubusercontent.com/64718777/167980670-952abf3a-fa3e-4f55-b4cb-9b711e797150.png)
![ss10](https://user-images.githubusercontent.com/64718777/160222573-67394226-9da5-428d-bc60-e41604a62cc2.png)

## Requirements

All requirements are listed in requirements.txt.

## Features

* Arithmetic operations
* Algebraic operations: Add/Subtract/Multiply exponentials, radicals and fractions.
* View history of computations.
* Live solve: Do operations in real time. 

## Technologies

* HTML
* CSS
* JavaScript
* Python
* Flask


## Testing

Unit tests for the backend are located in the 'Testing' folder and were written using the unittest library.
````
python -m unittest test_Methods.py
````

## Usage
Visit https://sky-labs.herokuapp.com/ or execute

````
set FLASK_APP=application.py 
flask run
````
in the terminal.

As of now, only operations done under the 'Algebra' tab are functional.

### Keywords
Keywords such as 'simplify' or 'combine' can be used before an expression to perform specific operations.
As of now, only two keywords are supported: 'simplify' and 'combine' for fractions.
![image](https://user-images.githubusercontent.com/64718777/160222426-e78cda86-eb72-4b59-a002-0915c613eabc.png)


## Contributors

* https://github.com/Skyjaheim2

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

Licensed under the [MIT License](LICENSE).

