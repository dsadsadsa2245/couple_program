from register import RegisterMixin, LoginMixin


class User(RegisterMixin, LoginMixin):
    pass
obj=User()
print(obj.register('jnfre',
                   'lgmdflsg',
                   'hhythyh',
                   '5yyy6gef',
                   '5yyy6gef'))
