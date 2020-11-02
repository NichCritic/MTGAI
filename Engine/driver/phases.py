class UntapPhase(object):
	def execute():
		raise_event("PHASING")
		raise_event("UNTAP")
		

class UpkeepPhase(object):
	def execute():
		raise_event("BEGINNING_OF_UPKEEP")
		handle_priority(active_player)
		

class DrawPhase(object):
	def execute():
		give_card(active_player)
		raise_event("BEGINNING_OF_DRAW_STEP")
		handle_priority(active_player)
		


class PreCombatMainPhase(object):
	def execute():
		raise_event("BEGINNING_OF_PRECOMBAT_MAIN_PHASE", "BEGINNING_OF_NEXT_MAIN_PHASE")
		handle_priority(active_player)
	

class BeginningOfCombatPhase(object):
	def execute():
		raise_event("BEGINNING_OF_COMBAT")
		handle_priority(active_player)
	

class DeclareAttackersPhase(object):
	def execute():
		declare_attackers(active_player)
		raise_event("ATTACKERS_DECLARED")
		handle_priority(active_player)

class DeclareBlockersPhase(object):
	def execute():
		declare_blockers(defending_player)
		assign_damage_order(active_player)
		assign_damage_order(defending_player)
		raise_event("BLOCKERS_DECLARED")
		handle_priority(active_player)
		handle_new_blockers(defending_player)


class CombatDamagePhase(object):
	def execute():
		assign_first_strike_damage()
		handle_damage()
		handle_priority(active_player)
		assign_damage()
		handle_damage()
		handle_priority(active_player)

class EndOfCombatPhase(object):
	pass

class PostCombatMainPhase(object):
	pass

class EndPhase(object):
	pass

class CleanupPhase(object):
	pass


