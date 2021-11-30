; Auto-generated. Do not edit!


(cl:in-package test-srv)


;//! \htmlinclude age-request.msg.html

(cl:defclass <age-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass age-request (<age-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <age-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'age-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test-srv:<age-request> is deprecated: use test-srv:age-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <age-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-srv:data-val is deprecated.  Use test-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <age-request>) ostream)
  "Serializes a message object of type '<age-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <age-request>) istream)
  "Deserializes a message object of type '<age-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<age-request>)))
  "Returns string type for a service object of type '<age-request>"
  "test/ageRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'age-request)))
  "Returns string type for a service object of type 'age-request"
  "test/ageRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<age-request>)))
  "Returns md5sum for a message object of type '<age-request>"
  "f7eb1611265559a9d645d68293c29871")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'age-request)))
  "Returns md5sum for a message object of type 'age-request"
  "f7eb1611265559a9d645d68293c29871")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<age-request>)))
  "Returns full string definition for message of type '<age-request>"
  (cl:format cl:nil "#request~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'age-request)))
  "Returns full string definition for message of type 'age-request"
  (cl:format cl:nil "#request~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <age-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <age-request>))
  "Converts a ROS message object to a list"
  (cl:list 'age-request
    (cl:cons ':data (data msg))
))
;//! \htmlinclude age-response.msg.html

(cl:defclass <age-response> (roslisp-msg-protocol:ros-message)
  ((flag
    :reader flag
    :initarg :flag
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass age-response (<age-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <age-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'age-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test-srv:<age-response> is deprecated: use test-srv:age-response instead.")))

(cl:ensure-generic-function 'flag-val :lambda-list '(m))
(cl:defmethod flag-val ((m <age-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-srv:flag-val is deprecated.  Use test-srv:flag instead.")
  (flag m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <age-response>) ostream)
  "Serializes a message object of type '<age-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'flag) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <age-response>) istream)
  "Deserializes a message object of type '<age-response>"
    (cl:setf (cl:slot-value msg 'flag) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<age-response>)))
  "Returns string type for a service object of type '<age-response>"
  "test/ageResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'age-response)))
  "Returns string type for a service object of type 'age-response"
  "test/ageResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<age-response>)))
  "Returns md5sum for a message object of type '<age-response>"
  "f7eb1611265559a9d645d68293c29871")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'age-response)))
  "Returns md5sum for a message object of type 'age-response"
  "f7eb1611265559a9d645d68293c29871")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<age-response>)))
  "Returns full string definition for message of type '<age-response>"
  (cl:format cl:nil "#response~%bool flag~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'age-response)))
  "Returns full string definition for message of type 'age-response"
  (cl:format cl:nil "#response~%bool flag~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <age-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <age-response>))
  "Converts a ROS message object to a list"
  (cl:list 'age-response
    (cl:cons ':flag (flag msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'age)))
  'age-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'age)))
  'age-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'age)))
  "Returns string type for a service object of type '<age>"
  "test/age")