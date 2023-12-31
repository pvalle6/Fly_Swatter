from Fly_Swatter.Fly_Swatter import mode_control, fire_mode, search, radar, target, graph_trajectory


args_ = mode_control.system_run_args(3, 10, None, True, True, 0, False)

db_ = mode_control.system_run(args_)

#print(db_.contacts)

print(db_.contacts)
