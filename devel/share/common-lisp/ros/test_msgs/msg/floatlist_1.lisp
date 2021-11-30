; Auto-generated. Do not edit!


(cl:in-package test_msgs-msg)


;//! \htmlinclude floatlist_1.msg.html

(cl:defclass <floatlist_1> (roslisp-msg-protocol:ros-message)
  ((flag
    :reader flag
    :initarg :flag
    :type cl:boolean
    :initform cl:nil)
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

(cl:defclass floatlist_1 (<floatlist_1>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <floatlist_1>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'floatlist_1)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_msgs-msg:<floatlist_1> is deprecated: use test_msgs-msg:floatlist_1 instead.")))

(cl:ensure-generic-function 'flag-val :lambda-list '(m))
(cl:defmethod flag-val ((m <floatlist_1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:flag-val is deprecated.  Use test_msgs-msg:flag instead.")
  (flag m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <floatlist_1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:x-val is deprecated.  Use test_msgs-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <floatlist_1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:y-val is deprecated.  Use test_msgs-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'idx-val :lambda-list '(m))
(cl:defmethod idx-val ((m <floatlist_1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_msgs-msg:idx-val is deprecated.  Use test_msgs-msg:idx instead.")
  (idx m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <floatlist_1>) ostream)
  "Serializes a message object of type '<floatlist_1>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'flag) 1 0)) ostream)
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <floatlist_1>) istream)
  "Deserializes a message object of type '<floatlist_1>"
    (cl:setf (cl:slot-value msg 'flag) (cl:not (cl:zerop (cl:read-byte istream))))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<floatlist_1>)))
  "Returns string type for a message object of type '<floatlist_1>"
  "test_msgs/floatlist_1")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'floatlist_1)))
  "Returns string type for a message object of type 'floatlist_1"
  "test_msgs/floatlist_1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<floatlist_1>)))
  "Returns md5sum for a message object of type '<floatlist_1>"
  "b14086f7038ce2afa371784cb7fd9953")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'floatlist_1)))
  "Returns md5sum for a message object of type 'floatlist_1"
  "b14086f7038ce2afa371784cb7fd9953")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<floatlist_1>)))
  "Returns full string definition for message of type '<floatlist_1>"
  (cl:format cl:nil "bool flag~%float64 x~%float64 y~%int8 idx~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'floatlist_1)))
  "Returns full string definition for message of type 'floatlist_1"
  (cl:format cl:nil "bool flag~%float64 x~%float64 y~%int8 idx~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <floatlist_1>))
  (cl:+ 0
     1
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <floatlist_1>))
  "Converts a ROS message object to a list"
  (cl:list 'floatlist_1
    (cl:cons ':flag (flag msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':idx (idx msg))
))
