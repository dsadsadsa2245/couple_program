# """CRUD - Create, Read(listing, detail), Update, Delet"""
# class CreateMixin:
#     def _get_or_set_objects_and_id(self):
#         try:
#             self.id
#             self.objects
#         except (NameError,AttributeError):
#             self.objects=[]
#             self.id=0
#     def __init__(self):
#         self._get_or_set_objects_and_id()
#     def post(self, **kwargs):
#         self.id +=1
#         obj = dict(id=self.id, **kwargs)
#         self.objects.append(obj)
#         return {'status':'201 created', 'msg':obj}
# # create=CreateMixin()
# # create.post(title='Samsung' , description='это описание нашего товара', price=900, qty=5)
# class ReadMixin:
#     def list_(self):
#         res=[{'id':obj['id'], 'title':obj['title']}for obj in self.objects]
#         return {'status':'200 Ok','msg':res}
#     def detail(self, id, **kwargs):
#         for product in self.objects:
#             if product['id']== id:
#                 return product
#         return {'msg':'Error'}
