import physics


if (__name__=="__main__"):
    while(True):
        physics.PhysicsSingleton.run()
        print(physics.PhysicsSingleton.body.position)