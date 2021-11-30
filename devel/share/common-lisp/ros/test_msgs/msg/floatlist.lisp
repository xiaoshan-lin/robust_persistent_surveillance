; Auto-generated. Do not edit!


(cl:in-package test_msgs-msg)


;//! \htmlinclude floatlist.msg.html

(cl:defclass <floatlist> (roslisp-msg-protocol:ros-message)
  ((type
    :reader type
    :initarg :type
    :type cl:fixnum
    :initform 0)
   (x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (idx
    :reader idx
    :initarg :idx
    :type cl:fixnum
    :initform 0))
)

(cl:defclass floatlist (<floatlist>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <floatlist>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'floatlist)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_msgs-msg:<floatlist> is deprecated: use test_msgs-msg:floatlist instead.")))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <floatlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:type-val is deprecated.  Use test_msgs-msg:type instead.")
  (type m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <floatlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:x-val is deprecated.  Use test_msgs-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <floatlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:y-val is deprecated.  Use test_msgs-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'idx-val :lambda-list '(m))
(cl:defmethod idx-val ((m <floatlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:idx-val is deprecated.  Use test_msgs-msg:idx instead.")
  (idx m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <floatlist>) ostream)
  "Serializes a message object of type '<floatlist>"
  (cl:let* ((signed (cl:slot-value msg 'type)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'idx)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <floatlist>) istream)
  "Deserializes a message object of type '<floatlist>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'type) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'idx) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<floatlist>)))
  "Returns string type for a message object of type '<floatlist>"
  "test_msgs/floatlist")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'floatlist)))
  "Returns string type for a message object of type 'floatlist"
  "test_msgs/floatlist")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<floatlist>)))
  "Returns md5sum for a message object of type '<floatlist>"
  "eb0aebf20b775fdee3c748e774f21882")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'floatlist)))
  "Returns md5sum for a message object of type 'floatlist"
  "eb0aebf20b775fdee3c748e774f21882")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<floatlist>)))
  "Returns full string definition for message of type '<floatlist>"
  (cl:format cl:nil "int8 type~%float64 x~%float64 y~%int8 idx~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'floatlist)))
  "Returns full string definition for message of type 'floatlist"
  (cl:format cl:nil "int8 type~%float64 x~%float64 y~%int8 idx~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <floatlist>))
  (cl:+ 0
     1
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <floatlist>))
  "Converts a ROS message object to a list"
  (cl:list 'floatlist
    (cl:cons ':type (type msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':idx (idx msg))
))
