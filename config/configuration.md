# **Configuring an 'object' in the generic configuration language**
# Defines the object <identifier> which inherits from <baseType>
#
# [<baseType>_<identifier>]

[sensor_test-temperature]
# default config at './config/test_temperature/'
# custom config overwrites the default config
# config = "conf/my-cfg"
#
# Yes to add all unconfigured values from the default config
# mergeConfig = "No"

# Values set here are added afterwards and overwrite values from other configs
# <optionName> = <optionValue>

maxValue = 45
