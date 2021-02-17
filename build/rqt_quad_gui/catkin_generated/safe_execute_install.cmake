execute_process(COMMAND "/home/xslin/Documents/xslin/research/rpg_ws/build/rqt_quad_gui/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/xslin/Documents/xslin/research/rpg_ws/build/rqt_quad_gui/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
