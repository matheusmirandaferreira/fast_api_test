from http import HTTPStatus

def test_read_root_deve_retornar_ok():
  ...

def test_create_user(client):
  response = client.post(
    '/users', 
    json={
      'name': 'teste',
      'password': 'senha',
      'email': 'teste@teste.com'
    }
  )

  # validar STATUS CODE
  assert response.status_code == HTTPStatus.CREATED

  
  # validar UserSchemaResponse
  assert response.json() == {
    'name': 'teste',
    'email': 'teste@teste.com',
    'id': 1
  }

def test_read_users(client):
  response = client.get('/users')

  assert response.status_code == HTTPStatus.OK

  assert response.json() == {
    'users':[
      {
        'name': 'teste',
        'email': 'teste@teste.com',
        'id': 1
      }
    ]
  }

def test_update_user(client):
  response = client.put(
    '/users/1',
    json={
        'name': 'teste editado',
        'email': 'editei@email.com',
        'id': 1,
        'password': 'string'
      }
    )
  
  assert response.json() == {
      'name': 'teste editado',
      'email': 'editei@email.com',
      'id': 1,
  }

def test_delete_user(client):
  response = client.delete('/users/1')

  assert response.json() == {
    'message': 'User deleted'
  }
