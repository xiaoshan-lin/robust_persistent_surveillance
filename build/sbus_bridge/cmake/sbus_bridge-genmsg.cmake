# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "sbus_bridge: 1 messages, 0 services")

set(MSG_I_FLAGS "-Isbus_bridge:/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg;-Iquadrotor_msgs:/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_common/quadrotor_msgs/msg;-Iroscpp:/opt/ros/melodic/share/roscpp/cmake/../msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Inav_msgs:/opt/ros/melodic/share/nav_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(sbus_bridge_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg" NAME_WE)
add_custom_target(_sbus_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sbus_bridge" "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(sbus_bridge
  "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sbus_bridge
)

### Generating Services

### Generating Module File
_generate_module_cpp(sbus_bridge
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sbus_bridge
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(sbus_bridge_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(sbus_bridge_generate_messages sbus_bridge_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg" NAME_WE)
add_dependencies(sbus_bridge_generate_messages_cpp _sbus_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sbus_bridge_gencpp)
add_dependencies(sbus_bridge_gencpp sbus_bridge_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sbus_bridge_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(sbus_bridge
  "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sbus_bridge
)

### Generating Services

### Generating Module File
_generate_module_eus(sbus_bridge
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sbus_bridge
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(sbus_bridge_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(sbus_bridge_generate_messages sbus_bridge_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg" NAME_WE)
add_dependencies(sbus_bridge_generate_messages_eus _sbus_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sbus_bridge_geneus)
add_dependencies(sbus_bridge_geneus sbus_bridge_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sbus_bridge_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(sbus_bridge
  "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sbus_bridge
)

### Generating Services

### Generating Module File
_generate_module_lisp(sbus_bridge
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sbus_bridge
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(sbus_bridge_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(sbus_bridge_generate_messages sbus_bridge_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg" NAME_WE)
add_dependencies(sbus_bridge_generate_messages_lisp _sbus_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sbus_bridge_genlisp)
add_dependencies(sbus_bridge_genlisp sbus_bridge_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sbus_bridge_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(sbus_bridge
  "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sbus_bridge
)

### Generating Services

### Generating Module File
_generate_module_nodejs(sbus_bridge
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sbus_bridge
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(sbus_bridge_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(sbus_bridge_generate_messages sbus_bridge_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg" NAME_WE)
add_dependencies(sbus_bridge_generate_messages_nodejs _sbus_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sbus_bridge_gennodejs)
add_dependencies(sbus_bridge_gennodejs sbus_bridge_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sbus_bridge_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(sbus_bridge
  "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sbus_bridge
)

### Generating Services

### Generating Module File
_generate_module_py(sbus_bridge
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sbus_bridge
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(sbus_bridge_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(sbus_bridge_generate_messages sbus_bridge_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xslin/Documents/xslin/research/rpg_ws/src/rpg_quadrotor_control/bridges/sbus_bridge/msg/SbusRosMessage.msg" NAME_WE)
add_dependencies(sbus_bridge_generate_messages_py _sbus_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sbus_bridge_genpy)
add_dependencies(sbus_bridge_genpy sbus_bridge_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sbus_bridge_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sbus_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sbus_bridge
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET quadrotor_msgs_generate_messages_cpp)
  add_dependencies(sbus_bridge_generate_messages_cpp quadrotor_msgs_generate_messages_cpp)
endif()
if(TARGET roscpp_generate_messages_cpp)
  add_dependencies(sbus_bridge_generate_messages_cpp roscpp_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(sbus_bridge_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sbus_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sbus_bridge
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET quadrotor_msgs_generate_messages_eus)
  add_dependencies(sbus_bridge_generate_messages_eus quadrotor_msgs_generate_messages_eus)
endif()
if(TARGET roscpp_generate_messages_eus)
  add_dependencies(sbus_bridge_generate_messages_eus roscpp_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(sbus_bridge_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sbus_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sbus_bridge
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET quadrotor_msgs_generate_messages_lisp)
  add_dependencies(sbus_bridge_generate_messages_lisp quadrotor_msgs_generate_messages_lisp)
endif()
if(TARGET roscpp_generate_messages_lisp)
  add_dependencies(sbus_bridge_generate_messages_lisp roscpp_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(sbus_bridge_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sbus_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sbus_bridge
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET quadrotor_msgs_generate_messages_nodejs)
  add_dependencies(sbus_bridge_generate_messages_nodejs quadrotor_msgs_generate_messages_nodejs)
endif()
if(TARGET roscpp_generate_messages_nodejs)
  add_dependencies(sbus_bridge_generate_messages_nodejs roscpp_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(sbus_bridge_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sbus_bridge)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sbus_bridge\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sbus_bridge
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET quadrotor_msgs_generate_messages_py)
  add_dependencies(sbus_bridge_generate_messages_py quadrotor_msgs_generate_messages_py)
endif()
if(TARGET roscpp_generate_messages_py)
  add_dependencies(sbus_bridge_generate_messages_py roscpp_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(sbus_bridge_generate_messages_py std_msgs_generate_messages_py)
endif()
