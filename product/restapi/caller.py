"""

    This file is auto generated by the case auto generator
    Swagger File: product.yaml
    Description: The Object Report for the API Definition
    API Doc Version: 1.0.0
    Date: 2020-04-16 16:48:10,

"""
from product.restapi.common.apicall import ApiCallBase
from .schemas import *


class ProductRestCall(ApiCallBase):
    def __init__(self, host, auth):
        super().__init__(host, auth, "http://127.0.0.1:5000/rest/", "http")

    @response_schema("200", ProductInfoList)
    @response_schema("500", ErrorResponse)
    def product_get(self, new_session=True):
        """
        Summary: Get product information
        Description: the product information
        URI: http://127.0.0.1:5000/rest//product
        METHOD: get
        """
        api_path = "product"
        response = self.api.get(api_path, new_session=new_session)
        return response

    @response_schema("201", ProductProductPostResponse201)
    @response_schema("400", ErrorResponse)
    @response_schema("500", ErrorResponse)
    def product_post(self, body, new_session=True):
        """
        Summary: Add new Product
        Description: 
        URI: http://127.0.0.1:5000/rest//product
        METHOD: post
        """
        api_path = "product"
        if isinstance(body, SchemaBase):
            call_data = body.to_dict()
        else:
            call_data = body

        response = self.api.post(api_path, data=call_data, new_session=new_session)
        return response

