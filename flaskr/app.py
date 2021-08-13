from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio
from .modelos import AlbumSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion,  VistaSignIn, VistaLogIn, VistaAlbum, VistaAlbumsUsuario, VistaCancionesAlbum
from flask_jwt_extended import JWTManager

from flask_cors import CORS

app = create_app(('default'))
app_context = app.app_context()
app_context.push() # to be consistent with each one of the modules in the app

db.init_app(app)
db.create_all()



api = Api(app) # initialize the API
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')

jwt = JWTManager(app) # to initialize the jwtmanager

cors = CORS(app)


#Prueba

with app.app_context():
    c = Cancion(titulo='Prueba',minutos=2, segundos=25,interprete="Ivan Penaloza")
    c2 = Cancion(titulo='Prueba2',minutos=2, segundos=25,interprete="Ivan Penaloza2")
    
    db.session.add(c)
    db.session.add(c2)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():
    u = Usuario(nombre='Ivan', contrasena='1234')
    a = Album(titulo='prueba',anio=1999,descripcion='texto',medio=Medio.CD)
    c = Cancion(titulo='mi cancion', minutos=1,segundos=15,interprete='Bunbury')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Cancion.query.all())
    # print(Cancion.query.all()[0].canciones)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all()) 

with app.app_context():
    album_schema = AlbumSchema()
    A = Album(titulo='Prueba', anio=1999, descripcion='Texto',medio = Medio.CD)
    db.session.add(A)
    db.session.commit()
    print([album_schema.dumps(album) for album in Album.query.all()])