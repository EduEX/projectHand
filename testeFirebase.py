import pyrebase

config = {
  'apiKey': "AIzaSyA0L-SbOntlvJ5fuyNancx9sTeR-SLPogw",
  'authDomain': "projetohandersonn.firebaseapp.com",
  'databaseURL': "https://projetohandersonn-default-rtdb.firebaseio.com",
  'projectId': "projetohandersonn",
  'storageBucket': "projetohandersonn.appspot.com",
  'messagingSenderId': "824444439419",
  'appId': "1:824444439419:web:48811a715616ddb2770bde"
}

firebase =  pyrebase.initialize_app(config)
storage = firebase.storage()
storage.child("foto1-1.jpg").put("pin.jpg")

#storage.download('imageNameDatabase.jpg', 'imageNameLocal.jpg')