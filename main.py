# Tech With Tim 
# In auth.py , I didnt use werkzeug.security module for security , instead i directly store the original pass without converting to cipher text 
# for that watch utube 1:43:00 logging users

from initial import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)