class Driver(object):
    pass


def priority_loop(game_state, p1, p2):
    # P1 puts things on the stack until they decline, then P2 puts things on the stack until they decline. If "things" > 0, then the other player gets a chance to put things on the stack
    # If both players pass resolve the top of the stack then repeat

    # List in reverse order
    pq = [p2, p1]
    action = (None, None)
    while not action == "PASS":
        p = pq.pop()
        actions = get_actions(game_state, p)
        p.send_actions(actions)
        action = wait_for_action(p)
        if not action == "PASS":
            stack = put_action_on_stack(action)
            pq.append(p)
            if stack and len(pq) == 1:
                pq.append(p2 if p == p1 else p1)
