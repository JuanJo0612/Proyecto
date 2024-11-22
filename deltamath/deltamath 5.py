def move_in_spiral(robot):
  for _ in range(8):
    while robot.can_move_forward():
      robot.move_forward()

    if robot.can_move_left():
      robot.rotate_left()
    elif robot.can_move_right():
      robot.rotate_right()
    else:
      robot.rotate_right()
      robot.rotate_right()