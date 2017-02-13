"""
    Iteration.fsm demonstrates nested iteration using the Iterate node
    and the =CNext=> transition, which waits for completion before advancing
    the iterator.  Use =Next=> if the source nodes don't need to
    complete.
"""

from cozmo_fsm import *

class Iteration(StateMachineProgram):
    def setup(self):
        """
    	outer_loop: Iterate(['alpha', 'bravo', 'charlie'])
    	outer_loop =SayData=> Say() =C=> inner_loop
    
              inner_loop: Iterate(4) =SayData=> Say() =CNext=> inner_loop
              inner_loop =CNext=> outer_loop
    
    	outer_loop =C=> Say('Done')
        """
        
        # Code generated by genfsm on Mon Feb 13 00:53:55 2017:
        self.name = self.__class__.__name__
        
        outer_loop = Iterate(['alpha', 'bravo', 'charlie']) .set_name("outer_loop") .set_parent(self)
        say1 = Say() .set_name("say1") .set_parent(self)
        inner_loop = Iterate(4) .set_name("inner_loop") .set_parent(self)
        say2 = Say() .set_name("say2") .set_parent(self)
        say3 = Say('Done') .set_name("say3") .set_parent(self)
        
        saydatatrans1 = SayDataTrans() .set_name("saydatatrans1")
        saydatatrans1 .add_sources(outer_loop) .add_destinations(say1)
        
        completiontrans1 = CompletionTrans() .set_name("completiontrans1")
        completiontrans1 .add_sources(say1) .add_destinations(inner_loop)
        
        saydatatrans2 = SayDataTrans() .set_name("saydatatrans2")
        saydatatrans2 .add_sources(inner_loop) .add_destinations(say2)
        
        cnexttrans1 = CNextTrans() .set_name("cnexttrans1")
        cnexttrans1 .add_sources(say2) .add_destinations(inner_loop)
        
        cnexttrans2 = CNextTrans() .set_name("cnexttrans2")
        cnexttrans2 .add_sources(inner_loop) .add_destinations(outer_loop)
        
        completiontrans2 = CompletionTrans() .set_name("completiontrans2")
        completiontrans2 .add_sources(outer_loop) .add_destinations(say3)
        
        return self
