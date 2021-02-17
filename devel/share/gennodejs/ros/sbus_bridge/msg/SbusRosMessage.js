// Auto-generated. Do not edit!

// (in-package sbus_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class SbusRosMessage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.channels = null;
      this.digital_channel_1 = null;
      this.digital_channel_2 = null;
      this.frame_lost = null;
      this.failsafe = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('channels')) {
        this.channels = initObj.channels
      }
      else {
        this.channels = new Array(16).fill(0);
      }
      if (initObj.hasOwnProperty('digital_channel_1')) {
        this.digital_channel_1 = initObj.digital_channel_1
      }
      else {
        this.digital_channel_1 = false;
      }
      if (initObj.hasOwnProperty('digital_channel_2')) {
        this.digital_channel_2 = initObj.digital_channel_2
      }
      else {
        this.digital_channel_2 = false;
      }
      if (initObj.hasOwnProperty('frame_lost')) {
        this.frame_lost = initObj.frame_lost
      }
      else {
        this.frame_lost = false;
      }
      if (initObj.hasOwnProperty('failsafe')) {
        this.failsafe = initObj.failsafe
      }
      else {
        this.failsafe = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SbusRosMessage
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Check that the constant length array field [channels] has the right length
    if (obj.channels.length !== 16) {
      throw new Error('Unable to serialize array field channels - length must be 16')
    }
    // Serialize message field [channels]
    bufferOffset = _arraySerializer.uint16(obj.channels, buffer, bufferOffset, 16);
    // Serialize message field [digital_channel_1]
    bufferOffset = _serializer.bool(obj.digital_channel_1, buffer, bufferOffset);
    // Serialize message field [digital_channel_2]
    bufferOffset = _serializer.bool(obj.digital_channel_2, buffer, bufferOffset);
    // Serialize message field [frame_lost]
    bufferOffset = _serializer.bool(obj.frame_lost, buffer, bufferOffset);
    // Serialize message field [failsafe]
    bufferOffset = _serializer.bool(obj.failsafe, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SbusRosMessage
    let len;
    let data = new SbusRosMessage(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [channels]
    data.channels = _arrayDeserializer.uint16(buffer, bufferOffset, 16)
    // Deserialize message field [digital_channel_1]
    data.digital_channel_1 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [digital_channel_2]
    data.digital_channel_2 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [frame_lost]
    data.frame_lost = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [failsafe]
    data.failsafe = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sbus_bridge/SbusRosMessage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '89ed6f5b79cb6f2d42c97b061bec3101';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
    # Regular 16 sbus channels with 11 bit value range each
    uint16[16] channels
    
    # Digital channels
    bool digital_channel_1
    bool digital_channel_2
    
    # Frame lost flag
    bool frame_lost
    
    # Failsafe flag
    bool failsafe
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SbusRosMessage(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.channels !== undefined) {
      resolved.channels = msg.channels;
    }
    else {
      resolved.channels = new Array(16).fill(0)
    }

    if (msg.digital_channel_1 !== undefined) {
      resolved.digital_channel_1 = msg.digital_channel_1;
    }
    else {
      resolved.digital_channel_1 = false
    }

    if (msg.digital_channel_2 !== undefined) {
      resolved.digital_channel_2 = msg.digital_channel_2;
    }
    else {
      resolved.digital_channel_2 = false
    }

    if (msg.frame_lost !== undefined) {
      resolved.frame_lost = msg.frame_lost;
    }
    else {
      resolved.frame_lost = false
    }

    if (msg.failsafe !== undefined) {
      resolved.failsafe = msg.failsafe;
    }
    else {
      resolved.failsafe = false
    }

    return resolved;
    }
};

module.exports = SbusRosMessage;
