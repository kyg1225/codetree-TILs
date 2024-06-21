class ProductCode:
    def __init__(self, p_name='codetree', p_code=50):
        self.p_name = p_name
        self.p_code = p_code

prod_code = ProductCode()
print(f'product {prod_code.p_code} is {prod_code.p_name}')

name, code = tuple(input().split())
prod_code = ProductCode(name, code)
print(f'product {prod_code.p_code} is {prod_code.p_name}')