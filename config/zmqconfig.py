#-*- coding: utf-8 -*-
import zmq

context = zmq.Context()
one_zmq_addr = "ipc://one_zmq_addr"
one_to_two_subject = "one_to_two_subject"
one_to_three_subject = "one_to_three_subject"

two_zmq_addr = "ipc://two_zmq_addr"
two_to_one_subject = "two_to_one_subject"
two_to_three_subject = "two_to_three_subject"

three_zmq_addr = "ipc://three_zmq_addr"
three_to_one_subject = "three_to_one_subject"
three_to_two_subject = "three_to_two_subject"