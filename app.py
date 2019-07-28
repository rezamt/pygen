import yaml
from yaml import Loader


def main():
    stack = yaml.load(open('stack.yml'), Loader=Loader)

    print "Input Stack Loaded"  # just for debugging
    print stack  # just for debugging

    # Output file
    tf = open("azure-vm.tf", "w")

    # Creating provider

    # Reading Provider
    providers = stack['provider']
    print providers  # just for debugging

    subscription_id = providers['subscription_id']
    client_id = providers['client_id']
    client_secret = providers['client_secret']
    tenant_id = providers['tenant_id']

    # Write data in HCL format back to terraform output file
    #   provider "azurerm" {
    #       subscription_id = "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    #       client_id = "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    #       client_secret = "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    #       tenant_id = "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    #   }


    tf.write("provider \"azurerm\" {\n")
    tf.write("\t subscription_id: \"{}\"\n".format(subscription_id))
    tf.write("\t client_id: \"{}\"\n".format(client_id))
    tf.write("\t client_secret: \"{}\"\n".format(client_secret))
    tf.write("\t tenant_id: \"{}\"\n".format(tenant_id))
    tf.write("}\n\n")

    tf.close()

if __name__ == '__main__':
    main()
