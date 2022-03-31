# Import the API app creation:
from api import create_app


# This is the flask app:
app = create_app()


# Main function:
def _main():
    app.run(debug=True)


# Run the script directly:
if __name__ == '__main__':
    _main()
    print('end of main.py')