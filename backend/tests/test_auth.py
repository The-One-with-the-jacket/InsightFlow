import unittest
from app import create_app, db
from app.models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/auth/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password',
            'password2': 'password'
        })
        self.assertEqual(response.status_code, 200)
        user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(user)

    def test_login(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        response = self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/auth/logout')
        self.assertEqual(response.status_code, 302)

    def test_password_reset_request(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        response = self.client.post('/auth/reset_password_request', data={
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 200)

    def test_password_reset(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        token = user.get_reset_password_token()
        response = self.client.post(f'/auth/reset_password/{token}', data={
            'password': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(user.check_password('newpassword'))

if __name__ == '__main__':
    unittest.main()
