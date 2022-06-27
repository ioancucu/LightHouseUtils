import tensorflow as tf; 
print ("gpu:9999999999999999999")
phDev = tf.config.list_physical_devices('GPU')
print("Num {phDev}", len(phDev))