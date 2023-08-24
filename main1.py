import falcon
import json
import logging
from wsgiref import simple_server

logging.basicConfig(filename='api_calling_logs.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
class Home:
    def on_get(self,req,res):
        wel="wellcome the falcon api"
        res.status = falcon.HTTP_200
        res.text = json.dumps(wel, indent=4)
        logging.info("home API called.")
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
            logging.info("AdditionResource API called.")
        except ValueError:
            resp.status = falcon.HTTP_400
            resp.text = "Invalid input. Please provide valid numeric parameters."
            logging.info("AdditionResource API called.")

class GetNameResource:
    def on_get(self, req, res):
        try:
            name = req.get_param("name")
            age = int(req.get_param("age"))

            if age < 18:
                message = f"Hello {name}, your age is not 18+."
            else:
                message = f"Hello {name}, your age {age} is 18+."

            response_data = {
                "message": message
            }

            response_text = f"{message}\nJSON Response:\n{json.dumps(response_data, indent=4)}"

            res.status = falcon.HTTP_200
            res.text = response_text
            logging.info("AdditionResource API called.")
        except ValueError:
            res.status = falcon.HTTP_400
            res.text = "Invalid input. Please provide valid parameters."
            logging.info("AdditionResource API called.")
            
class PostExampleResource:
    def on_post(self, req, res):
        try:
            data = json.loads(req.bounded_stream.read().decode('utf-8'))
            message = f"Received data: {data}"

            response_data = {
                "message": message
            }

            res.status = falcon.HTTP_200
            res.media = response_data
            logging.info("POST API called.")
            
        except json.JSONDecodeError:
            res.status = falcon.HTTP_400
            res.text = "Invalid JSON format in request body."
            
class PutExampleResource:
    def on_put(self, req, res):
        try:
            data = json.loads(req.bounded_stream.read().decode('utf-8'))
            message = f"Received data for update: {data}"

            response_data = {
                "message": message
            }

            res.status = falcon.HTTP_200
            res.media = response_data
            logging.info("PUT API called.")
        except json.JSONDecodeError:
            res.status = falcon.HTTP_400
            res.text = "Invalid JSON format in request body."
            
class deleteExampleResource:
    def on_delete(self, req, res):
        try:
            data = json.loads(req.bounded_stream.read().decode('utf-8'))
            message = f"Received data for delete: {data}"

            response_data = {
                "message": message
            }

            res.status = falcon.HTTP_200
            res.media = response_data
            logging.info("delete API called.")
            logging.info("DELETE API called.")
        except json.JSONDecodeError:
            res.status = falcon.HTTP_400
            res.text = "Invalid JSON format in request body."

class PatchExampleResource:
    def on_patch(self, req, res):
        try:
            data = json.loads(req.bounded_stream.read().decode('utf-8'))
            message = f"Received data for Patch Data : {data}"

            response_data = {
                "message": message
            }

            res.status = falcon.HTTP_200
            res.media = response_data
            logging.info("Patch API called.")
        except json.JSONDecodeError:
            res.status = falcon.HTTP_400
            res.text = "Invalid JSON format in request body."
            
class OptionsExampleResource:
    def on_options(self, req, res):
        # Define the allowed methods for the resource
        allowed_methods = ['GET', 'POST', 'PUT', 'DELETE','OPTION','HEAD']

        # Set the Allow header with the list of allowed methods
        res.set_header('Allow', ', '.join(allowed_methods))
        res.status = falcon.HTTP_200
        res.text = "Allowed methods: " + ', '.join(allowed_methods)
        logging.info(allowed_methods)
# Create a Falcon API instance
api = falcon.App()

# Add routes to the resources
api.add_route('/',Home())
api.add_route('/add', AdditionResource())
api.add_route('/getname', GetNameResource())
api.add_route('/newpost', PostExampleResource())
api.add_route('/putdata',PutExampleResource())
api.add_route('/deldata',deleteExampleResource())
api.add_route('/patchdata',PatchExampleResource())
api.add_route('/option',OptionsExampleResource())

# Run the combined API
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    print("Server started at http://127.0.0.1:8000")
    logging.info("Server started at http://127.0.0.1:8000")
    httpd.serve_forever()
