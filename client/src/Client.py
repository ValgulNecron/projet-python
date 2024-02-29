import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import MessageFactory

channel = grpc.insecure_channel('141.145.209.36:3333')
reflection_db = ProtoReflectionDescriptorDatabase(channel)
desc_pool = DescriptorPool(reflection_db)

# Example: Get service and method descriptors
service_desc = desc_pool.FindServiceByName("account.account")
print(service_desc)
method_desc = service_desc.FindMethodByName("account.account.CreateAccount")


# Example: Create a request message dynamically
request_desc = desc_pool.FindMessageTypeByName("helloworld.HelloRequest")
request = MessageFactory(desc_pool).GetPrototype(request_desc)()