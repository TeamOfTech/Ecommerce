import graphene
from graphene_django import DjangoObjectType

from .models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class Query(graphene.ObjectType):
    all_Products = graphene.List(ProductType)
    all_Categories = graphene.List(CategoryType)
    product = graphene.Field(ProductType, product_id=graphene.Int(required=True))
    product_by_category = graphene.Field(
        CategoryType, category=graphene.String(required=True)
    )

    def resolve_all_Categories(root, info):
        return Category.objects.all()

    def resolve_all_Products(root, info):
        return Product.objects.all()

    def resolve_product_by_category(root, info, category):
        try:
            return Category.objects.get(title=category)
        except Category.DoesNotExist:
            return None

    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)


schema = graphene.Schema(query=Query)
