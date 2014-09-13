blanky_googleAppEngine
======================

Base structure for developing Python Google App Engine app. 

### Installing:
* Download this project source code.
* [Download Google App Engine Python SDK](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
* [Download PyCharm because it is a great IDE for Python dev](http://www.jetbrains.com/pycharm/download/)
* Open up PyCharm, select "Open directory" and browse to this project's source code root.
* Run command to start local dev server:
`google_appengine_sdk_location/dev_appserver.py name_of_project_directory_renamed_above/
* Go to [http://localhost:8080/](http://localhost:8080/) to see your app in action! (You should see a "hello world" message).

### Optional things to do after installing:
* Rename the directory from `blanky_googleAppEngine` to the name of your app 
to make it more useful of a name.
* Rename `helloworld.py` to the name of your app. After renaming this file, you must also edit the line `helloworld.application` in 
the app.yaml	file as well. 
* Because the app.yaml already specifies static file directories for CSS stylesheets and picture files, create the directory `css` and 
`img` and put files in them.
* A web application that says "Hello world" is lame. Make it cool. Follow the [Google App Engine Quickstart tutorial](https://developers.google.com/appengine/docs/python/gettingstartedpython27/introduction) 
if you are a beginner to Google App Engine. As of creating this README file, I recommend the tutorial as I think it is very well done actually
and it is how I learned it. It may/may not have changed sense I last used it...