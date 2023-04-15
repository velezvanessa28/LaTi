from .models import Producto
from lati import delete_null_productos

def mi_vista(request):
    delete_null_productos()