''' Module with the users needed for this exercise '''

USERS = {}
ADD_USER = "INSERT INTO users (ID, username, role, password) VALUES (%s, %s, %s, %s)"

# Password = admin123
USERS['ADMIN'] = (1,'admin','superuser','6EF53DE837947336B4128FB681F252E1AC899ED66F1BB69715A3A3D79352180D0171E3353F5C009CB0AFC75316DB4D6D8B075060A3F36C57E502637B3B203C4D')

# Password = dpo123
USERS['PRIVACY'] = (2,'dpo','privacy','E5348E4B7410E38DD6D0D09F8A55FF4AA75FBA4091947A9EDC7D398473272C5668A83F9F2BD20D9788DBDB9CB86A33EB831196050A1E1A40CD30E1FCBE033910')

# Passowrd = payment123
USERS['FINANCE'] = (3,'payment','finance','1B71463C0D18A1B9691632DE15E8D9C6620AF8958DA23082FDB3F639A4852E9281E44A89B0E977BE5DC7F01AA509E9F1FC46B827BD8943CB3482BE7D9CBF5D97')

# Passowrd = user123
USERS['REGULAR'] = (4,'user','none','DA556993769A7B1B7C17CAC7689FF1D417E5AC267BF91396A84E2FA32E6E168663FC6D29DE752468691526C8B6B40939453E236F2E6A50C2187F9F1EF4C460F8')