import falcon
import json

class AdditionResource:
    def on_get(self, req, resp):
        try:
            num1 = float(req.get_param('num1'))
            num2 = float(req.get_param('num2'))

            result = {
                'addition of two number': num1 + num2,
                'substraction of two number': num1 - num2,
                'multiplication of two number': num1 * num2,
                'divison of two number': num1 / num2,
                'moduler of two number': num1 % num2
            }

            resp.status = falcon.HTTP_200
            resp.text = json.dumps(result, indent=4)
        except ValueError:
            resp.status = falcon.HTTP_400
            resp.text = "Invalid input. Please provide valid numeric parameters."

# Create a Falcon API instance
api = falcon.App()

# Add a route to the AdditionResource
api.add_route('/add', AdditionResource())
# if __name__ == '__main__':
#     from wsgiref import simple_server

#     httpd = simple_server.make_server('127.0.0.1', 8000, api)
#     print("Server started at http://127.0.0.1:8000")
#     httpd.serve_forever()


class getname:
    def on_get(self,req,res):
        name=req.get_param("name")
        age=int(req.get_param("age"))
        try:
            if(age<18):
                message=(f"hello {name} your age {age} is your not 18+")
            else:
                message=(f"Hello {name} your age {age} and your 18+")
            
            print(message)
            response_data = {
                "message": message
            }

            response_text = f"{message}\nJSON Response:\n{json.dumps(response_data, indent=4)}"

            res.status = falcon.HTTP_200
            res.text = response_text  
        except ValueError:
            res.status = falcon.HTTP_400
            res.text = "Invalid input. Please provide valid parameters."    
# Create a Falcon API instance
api = falcon.App()

# Add a route to the AdditionResource
api.add_route('/getname', getname())
    
# Run the API
if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    print("Server started at http://127.0.0.1:8000")
    httpd.serve_forever()
