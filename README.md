# ASCII-Image 🌆 

### ASCII Art Generator.

Convert your images to ASCII Art.

You can see how it works [here](http://ascii-image.herokuapp.com/)

![App Gif](/static/app.gif)

## Installation
1. Clone the code
2. Create virtual environment

  ```bash
  python -m venv env
  ```

3. Activate your virtual environment
  * Linux / Mac
  ```bash
  source env/bin/activate
  ```
  * Windows
  ```bash
  env\Scripts\activate.bat
  ```
4. Install dependecies
  ```python
  pip install -r requirements.txt
  ```

5. Run the code
  ```python
  python main.py
  # or
  gunicorn main:app
  ```

## Dependencies
+ Pillow
+ flask
+ gunicorn
+ flake8
