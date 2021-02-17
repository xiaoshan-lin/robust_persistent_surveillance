; Auto-generated. Do not edit!


(cl:in-package sbus_bridge-msg)


;//! \htmlinclude SbusRosMessage.msg.html

(cl:defclass <SbusRosMessage> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (channels
    :reader channels
    :initarg :channels
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 16 :element-type 'cl:fixnum :initial-element 0))
   (digital_channel_1
    :reader digital_channel_1
    :initarg :digital_channel_1
    :type cl:boolean
    :initform cl:nil)
   (digital_channel_2
    :reader digital_channel_2
    :initarg :digital_channel_2
    :type cl:boolean
    :initform cl:nil)
   (frame_lost
    :reader frame_lost
    :initarg :frame_lost
    :type cl:boolean
    :initform cl:nil)
   (failsafe
    :reader failsafe
    :initarg :failsafe
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SbusRosMessage (<SbusRosMessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SbusRosMessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SbusRosMessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sbus_bridge-msg:<SbusRosMessage> is deprecated: use sbus_bridge-msg:SbusRosMessage instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <SbusRosMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbus_bridge-msg:header-val is deprecated.  Use sbus_bridge-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'channels-val :lambda-list '(m))
(cl:defmethod channels-val ((m <SbusRosMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbus_bridge-msg:channels-val is deprecated.  Use sbus_bridge-msg:channels instead.")
  (channels m))

(cl:ensure-generic-function 'digital_channel_1-val :lambda-list '(m))
(cl:defmethod digital_channel_1-val ((m <SbusRosMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbus_bridge-msg:digital_channel_1-val is deprecated.  Use sbus_bridge-msg:digital_channel_1 instead.")
  (digital_channel_1 m))

(cl:ensure-generic-function 'digital_channel_2-val :lambda-list '(m))
(cl:defmethod digital_channel_2-val ((m <SbusRosMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbus_bridge-msg:digital_channel_2-val is deprecated.  Use sbus_bridge-msg:digital_channel_2 instead.")
  (digital_channel_2 m))

(cl:ensure-generic-function 'frame_lost-val :lambda-list '(m))
(cl:defmethod frame_lost-val ((m <SbusRosMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbus_bridge-msg:frame_lost-val is deprecated.  Use sbus_bridge-msg:frame_lost instead.")
  (frame_lost m))

(cl:ensure-generic-function 'failsafe-val :lambda-list '(m))
(cl:defmethod failsafe-val ((m <SbusRosMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbus_bridge-msg:failsafe-val is deprecated.  Use sbus_bridge-msg:failsafe instead.")
  (failsafe m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SbusRosMessage>) ostream)
  "Serializes a message object of type '<SbusRosMessage>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream))
   (cl:slot-value msg 'channels))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'digital_channel_1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'digital_channel_2) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'frame_lost) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'failsafe) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SbusRosMessage>) istream)
  "Deserializes a message object of type '<SbusRosMessage>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:setf (cl:slot-value msg 'channels) (cl:make-array 16))
  (cl:let ((vals (cl:slot-value msg 'channels)))
    (cl:dotimes (i 16)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'digital_channel_1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'digital_channel_2) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'frame_lost) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'failsafe) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SbusRosMessage>)))
  "Returns string type for a message object of type '<SbusRosMessage>"
  "sbus_bridge/SbusRosMessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SbusRosMessage)))
  "Returns string type for a message object of type 'SbusRosMessage"
  "sbus_bridge/SbusRosMessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SbusRosMessage>)))
  "Returns md5sum for a message object of type '<SbusRosMessage>"
  "89ed6f5b79cb6f2d42c97b061bec3101")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SbusRosMessage)))
  "Returns md5sum for a message object of type 'SbusRosMessage"
  "89ed6f5b79cb6f2d42c97b061bec3101")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SbusRosMessage>)))
  "Returns full string definition for message of type '<SbusRosMessage>"
  (cl:format cl:nil "Header header~%~%# Regular 16 sbus channels with 11 bit value range each~%uint16[16] channels~%~%# Digital channels~%bool digital_channel_1~%bool digital_channel_2~%~%# Frame lost flag~%bool frame_lost~%~%# Failsafe flag~%bool failsafe~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SbusRosMessage)))
  "Returns full string definition for message of type 'SbusRosMessage"
  (cl:format cl:nil "Header header~%~%# Regular 16 sbus channels with 11 bit value range each~%uint16[16] channels~%~%# Digital channels~%bool digital_channel_1~%bool digital_channel_2~%~%# Frame lost flag~%bool frame_lost~%~%# Failsafe flag~%bool failsafe~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SbusRosMessage>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'channels) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SbusRosMessage>))
  "Converts a ROS message object to a list"
  (cl:list 'SbusRosMessage
    (cl:cons ':header (header msg))
    (cl:cons ':channels (channels msg))
    (cl:cons ':digital_channel_1 (digital_channel_1 msg))
    (cl:cons ':digital_channel_2 (digital_channel_2 msg))
    (cl:cons ':frame_lost (frame_lost msg))
    (cl:cons ':failsafe (failsafe msg))
))
