# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from nubot_common/BallInfo.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import nubot_common.msg
import std_msgs.msg

class BallInfo(genpy.Message):
  _md5sum = "06211c2a8d639c68390f487a28e6a33a"
  _type = "nubot_common/BallInfo"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
int32     ballinfostate
Point2d   pos
PPoint    real_pos
Point2d   velocity
bool      pos_known
bool      velocity_known


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
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: nubot_common/Point2d
float32 x
float32 y

================================================================================
MSG: nubot_common/PPoint
float32 angle
float32 radius
"""
  __slots__ = ['header','ballinfostate','pos','real_pos','velocity','pos_known','velocity_known']
  _slot_types = ['std_msgs/Header','int32','nubot_common/Point2d','nubot_common/PPoint','nubot_common/Point2d','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,ballinfostate,pos,real_pos,velocity,pos_known,velocity_known

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BallInfo, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.ballinfostate is None:
        self.ballinfostate = 0
      if self.pos is None:
        self.pos = nubot_common.msg.Point2d()
      if self.real_pos is None:
        self.real_pos = nubot_common.msg.PPoint()
      if self.velocity is None:
        self.velocity = nubot_common.msg.Point2d()
      if self.pos_known is None:
        self.pos_known = False
      if self.velocity_known is None:
        self.velocity_known = False
    else:
      self.header = std_msgs.msg.Header()
      self.ballinfostate = 0
      self.pos = nubot_common.msg.Point2d()
      self.real_pos = nubot_common.msg.PPoint()
      self.velocity = nubot_common.msg.Point2d()
      self.pos_known = False
      self.velocity_known = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i6f2B.pack(_x.ballinfostate, _x.pos.x, _x.pos.y, _x.real_pos.angle, _x.real_pos.radius, _x.velocity.x, _x.velocity.y, _x.pos_known, _x.velocity_known))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pos is None:
        self.pos = nubot_common.msg.Point2d()
      if self.real_pos is None:
        self.real_pos = nubot_common.msg.PPoint()
      if self.velocity is None:
        self.velocity = nubot_common.msg.Point2d()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 30
      (_x.ballinfostate, _x.pos.x, _x.pos.y, _x.real_pos.angle, _x.real_pos.radius, _x.velocity.x, _x.velocity.y, _x.pos_known, _x.velocity_known,) = _struct_i6f2B.unpack(str[start:end])
      self.pos_known = bool(self.pos_known)
      self.velocity_known = bool(self.velocity_known)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i6f2B.pack(_x.ballinfostate, _x.pos.x, _x.pos.y, _x.real_pos.angle, _x.real_pos.radius, _x.velocity.x, _x.velocity.y, _x.pos_known, _x.velocity_known))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pos is None:
        self.pos = nubot_common.msg.Point2d()
      if self.real_pos is None:
        self.real_pos = nubot_common.msg.PPoint()
      if self.velocity is None:
        self.velocity = nubot_common.msg.Point2d()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 30
      (_x.ballinfostate, _x.pos.x, _x.pos.y, _x.real_pos.angle, _x.real_pos.radius, _x.velocity.x, _x.velocity.y, _x.pos_known, _x.velocity_known,) = _struct_i6f2B.unpack(str[start:end])
      self.pos_known = bool(self.pos_known)
      self.velocity_known = bool(self.velocity_known)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_i6f2B = struct.Struct("<i6f2B")