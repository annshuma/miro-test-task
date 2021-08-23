from const import SignInMessages


class TestSignInError:
    def test_error_sign_in(self, sign_in):
        sign_in.sign_in(email='test@test.test', password='Qwerty123$')
        assert sign_in.successfully_message == SignInMessages.SIGN_UP_ERROR_MESSAGE
