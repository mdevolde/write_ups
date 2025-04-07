#!/usr/bin/env python3

from z3 import *
import re

constraints_text = r'''
  if (local_3a == 0x32) {
    bump(0,&score);
  }
  if ((local_36 ^ local_3d) == 0xaa) {
    bump(0,&score);
  }
  if ((byte)(local_36 + local_27) == -0x70) {
    bump(0,&score);
  }
  if ((byte)(local_1a + local_31) == -0x7f) {
    bump(0,&score);
  }
  if (local_48 == 0xbe) {
    bump(0,&score);
  }
  if (local_35 == 100) {
    bump(0,&score);
  }
  if (local_3b == 0x31) {
    bump(0,&score);
  }
  if (local_2b == 0x39) {
    bump(0,&score);
  }
  if ((byte)(local_28 + local_16) == -0x6d) {
    bump(0,&score);
  }
  if (local_23 == 0x31) {
    bump(0,&score);
  }
  if ((byte)(local_54 + local_46) == '8') {
    bump(0,&score);
  }
  if ((local_48 ^ local_32) == 0x8e) {
    bump(0,&score);
  }
  if ((local_54 ^ local_27) == 0x71) {
    bump(0,&score);
  }
  if (local_2b == 0xb4) {
    bump(0,&score);
  }
  if (local_42 == 0x36) {
    bump(0,&score);
  }
  if (local_39 == local_25) {
    bump(&score);
  }
  if ((local_4b ^ local_34) == 3) {
    bump(0,&score);
  }
  if (local_37 == 0x76) {
    bump(0,&score);
  }
  if (local_50 == 0x32) {
    bump(0,&score);
  }
  if ((local_54 ^ local_25) == 0x85) {
    bump(0,&score);
  }
  if (local_53 == 0x54) {
    bump(0,&score);
  }
  if (local_3e == 0xe1) {
    bump(0,&score);
  }
  if ((local_4c ^ local_1f) == 0x81) {
    bump(0,&score);
  }
  if ((byte)(local_20 + local_3b) == 'a') {
    bump(0,&score);
  }
  if ((local_43 ^ local_1c) == 7) {
    bump(0,&score);
  }
  if ((local_43 ^ local_50) == 0x56) {
    bump(0,&score);
  }
  if ((byte)(local_47 + local_20) == 'f') {
    bump(0,&score);
  }
  if ((local_25 ^ local_1d) == 0x54) {
    bump(0,&score);
  }
  if (local_21 == 0xe5) {
    bump(0,&score);
  }
  if (local_31 == 'o') {
    bump(0,&score);
  }
  if ((byte)(local_30 + local_37) == 'f') {
    bump(0,&score);
  }
  if (local_23 == 0x31) {
    bump(0,&score);
  }
  if (local_3e == 0x38) {
    bump(0,&score);
  }
  if (local_2e == '4') {
    bump(0,&score);
  }
  if ((byte)(local_1d + local_42) == -0x69) {
    bump(0,&score);
  }
  if ((local_42 ^ local_23) == 0x2d) {
    bump(0,&score);
  }
  if ((byte)(local_33 + local_54) == -0x5c) {
    bump(0,&score);
  }
  if ((byte)(local_26 + local_2f) == -0xc) {
    bump(0,&score);
  }
  if ((byte)(local_3a + local_26) == -0x69) {
    bump(0,&score);
  }
  if ((byte)(local_26 + local_4b) == -0x6a) {
    bump(0,&score);
  }
  if (local_53 == 0x72) {
    bump(0,&score);
  }
  if (local_1a == 0x36) {
    bump(0,&score);
  }
  if (local_39 == 0xb1) {
    bump(0,&score);
  }
  if ((local_4d ^ local_1b) == 8) {
    bump(0,&score);
  }
  if ((local_53 ^ local_27) == 0x3a) {
    bump(0,&score);
  }
  if (local_1a == 0x44) {
    bump(0,&score);
  }
  if (local_1c == 0x12) {
    bump(0,&score);
  }
  if ((local_44 ^ local_2d) == 0x5b) {
    bump(0,&score);
  }
  if (local_2c == 0x2a) {
    bump(0,&score);
  }
  if (local_2c == 0x33) {
    bump(0,&score);
  }
  if ((byte)(local_3b + local_2f) == '?') {
    bump(0,&score);
  }
  if ((local_18 ^ local_55) == 0x60) {
    bump(0,&score);
  }
  if (local_40 == 0x24) {
    bump(0,&score);
  }
  if ((byte)(local_50 + local_2a) == '-') {
    bump(0,&score);
  }
  if (local_1c == 99) {
    bump(0,&score);
  }
  if ((local_1e ^ local_21) == 5) {
    bump(0,&score);
  }
  if (local_51 == 0x7b) {
    bump(0,&score);
  }
  if ((byte)(local_45 + local_4c) == -0x53) {
    bump(0,&score);
  }
  if ((byte)(local_3f + local_28) == -0x68) {
    bump(0,&score);
  }
  if (local_3d == 0x32) {
    bump(0,&score);
  }
  if (local_25 == 0x35) {
    bump(0,&score);
  }
  if ((local_1f ^ local_42) == 0x5b) {
    bump(0,&score);
  }
  if ((byte)(local_1f + local_47) == -0x67) {
    bump(0,&score);
  }
  if (local_20 == 0xd2) {
    bump(0,&score);
  }
  if ((local_55 ^ local_25) == 0x65) {
    bump(0,&score);
  }
  if ((byte)(local_2b + local_24) == -0x66) {
    bump(0,&score);
  }
  if ((byte)(local_41 + local_38) == -0x6a) {
    bump(0,&score);
  }
  if ((local_2d ^ local_23) == 0xda) {
    bump(0,&score);
  }
  if ((byte)(local_19 + local_35) == -0x6a) {
    bump(0,&score);
  }
  if ((byte)(local_2e + local_4e) == -0x68) {
    bump(0,&score);
  }
  if (local_23 == local_4b) {
    bump(&score);
  }
  if ((local_1c ^ local_4b) == 0x52) {
    bump(0,&score);
  }
  if (local_1d == 0x61) {
    bump(0,&score);
  }
  if (local_41 == 0x61) {
    bump(0,&score);
  }
  if ((local_17 ^ local_4d) == 1) {
    bump(0,&score);
  }
  if ((local_29 ^ local_33) == 0x30) {
    bump(0,&score);
  }
  if (local_34 == 0x32) {
    bump(0,&score);
  }
  if ((local_26 ^ local_24) == 4) {
    bump(0,&score);
  }
  if ((local_3a ^ local_3f) == 0x53) {
    bump(0,&score);
  }
  if ((byte)(local_55 + local_2c) == -0x7d) {
    bump(0,&score);
  }
  if (local_43 == 0xf1) {
    bump(0,&score);
  }
  if (local_39 == 0x35) {
    bump(0,&score);
  }
  if (local_45 == 0xd3) {
    bump(0,&score);
  }
  if ((byte)(local_4f + local_26) == -0x67) {
    bump(0,&score);
  }
  if ((byte)(local_39 + local_3c) == -0x51) {
    bump(0,&score);
  }
  if ((byte)(local_16 + local_42) == -0x4d) {
    bump(0,&score);
  }
  if (local_38 == 0x35) {
    bump(0,&score);
  }
  if (local_18 == 0x30) {
    bump(0,&score);
  }
  if ((byte)(local_46 + local_3c) == -0x7b) {
    bump(0,&score);
  }
  if ((local_41 ^ local_18) == 0x4f) {
    bump(0,&score);
  }
  if ((local_3a ^ local_23) == 3) {
    bump(0,&score);
  }
  if ((byte)(local_17 + local_22) == 'b') {
    bump(0,&score);
  }
  if ((byte)(local_41 + local_29) == -0x3b) {
    bump(0,&score);
  }
  if ((byte)(local_2a + local_43) == -0x37) {
    bump(0,&score);
  }
  if ((byte)(local_4c + local_31) == 'h') {
    bump(0,&score);
  }
  if (local_4c == local_42) {
    bump(&score);
  }
  if ((local_42 ^ local_34) == 4) {
    bump(0,&score);
  }
  if ((byte)(local_1e + local_55) == -0x7b) {
    bump(0,&score);
  }
  if (local_3f == 0x61) {
    bump(0,&score);
  }
  if (local_44 == 0x39) {
    bump(0,&score);
  }
  if (local_4b == 0x31) {
    bump(0,&score);
  }
  if (local_20 == 0x30) {
    bump(0,&score);
  }
  if ((byte)(local_24 + local_18) == -0x17) {
    bump(0,&score);
  }
  if (local_23 == 0x31) {
    bump(0,&score);
  }
  if ((byte)(local_1e + local_52) == -0x41) {
    bump(0,&score);
  }
  if ((byte)(local_28 + local_3c) == -0x67) {
    bump(0,&score);
  }
  if (local_27 == 0x32) {
    bump(0,&score);
  }
  if ((byte)(local_3d + local_2a) == -0x69) {
    bump(0,&score);
  }
  if (local_3b == 0x31) {
    bump(0,&score);
  }
  if (local_47 == 0x36) {
    bump(0,&score);
  }
  if ((byte)(local_52 + local_17) == 'v') {
    bump(0,&score);
  }
  if (local_3a == 0x32) {
    bump(0,&score);
  }
  if ((local_16 ^ local_28) == 0x4a) {
    bump(0,&score);
  }
  if ((byte)(local_29 + local_47) == -0x10) {
    bump(0,&score);
  }
  if (local_4c == 0xd8) {
    bump(0,&score);
  }
  if ((byte)(local_1b + local_17) == 'b') {
    bump(0,&score);
  }
  if ((byte)(local_18 + local_3f) == -0x6d) {
    bump(0,&score);
  }
  if ((local_22 ^ local_20) == 2) {
    bump(0,&score);
  }
  if (local_3a == 0x32) {
    bump(0,&score);
  }
  if ((local_23 ^ local_1a) == 7) {
    bump(0,&score);
  }
  if (local_21 == 0x30) {
    bump(0,&score);
  }
  if (local_34 == 0x79) {
    bump(0,&score);
  }
  if (local_18 == 0x33) {
    bump(0,&score);
  }
  if ((byte)(local_40 + local_24) == -0x3b) {
    bump(0,&score);
  }
  if (local_31 == 'S') {
    bump(0,&score);
  }
  if (local_46 == 9) {
    bump(0,&score);
  }
  if ((byte)(local_55 + local_35) == -0x4c) {
    bump(0,&score);
  }
  if ((byte)(local_47 + local_22) == 'h') {
    bump(0,&score);
  }
  if ((local_2a ^ local_47) == 0xfb) {
    bump(0,&score);
  }
  if (local_1b == 0x4f) {
    bump(0,&score);
  }
  if (local_4b == 0x3e) {
    bump(0,&score);
  }
  if (local_26 == 0xec) {
    bump(0,&score);
  }
  if (local_28 == 0x37) {
    bump(0,&score);
  }
  if ((byte)(local_3f + local_1a) == -1) {
    bump(0,&score);
  }
  if ((local_3d ^ local_53) == 0x28) {
    bump(0,&score);
  }
  if (local_25 == 0xd1) {
    bump(0,&score);
  }
  if ((local_1e ^ local_4e) == 0xe8) {
    bump(0,&score);
  }
  if (local_26 == 0x65) {
    bump(0,&score);
  }
  if ((byte)(local_50 + local_1c) == -4) {
    bump(0,&score);
  }
  if ((byte)(local_3d + local_50) == 'd') {
    bump(0,&score);
  }
  if ((local_33 ^ local_1f) == 2) {
    bump(0,&score);
  }
  if (local_4c == 0x36) {
    bump(0,&score);
  }
  if (local_50 == 0x32) {
    bump(0,&score);
  }
  if (local_3b == 0x31) {
    bump(0,&score);
  }
  if (local_19 == 0x32) {
    bump(0,&score);
  }
  if ((byte)(local_51 + local_4e) == -0x21) {
    bump(0,&score);
  }
  if (local_36 == 0x34) {
    bump(0,&score);
  }
  if ((local_23 ^ local_21) == 0x59) {
    bump(0,&score);
  }
  if (local_1b == 0x39) {
    bump(0,&score);
  }
  if ((local_49 ^ local_2a) == 0x53) {
    bump(0,&score);
  }
  if (local_4e == 0x61) {
    bump(0,&score);
  }
  if ((local_20 ^ local_4e) == 0x54) {
    bump(0,&score);
  }
  if ((byte)(local_1a + local_4f) == 'j') {
    bump(0,&score);
  }
  if ((byte)(local_44 + local_39) == 'n') {
    bump(0,&score);
  }
  if (local_51 == 0x7b) {
    bump(0,&score);
  }
  if (local_32 == 0x65) {
    bump(0,&score);
  }
  if ((byte)(local_31 + local_29) == -0x6a) {
    bump(0,&score);
  }
  if (local_16 == 0x7d) {
    bump(0,&score);
  }
  if ((local_3a ^ local_2c) == 0x5d) {
    bump(0,&score);
  }
  if (local_2d == 0x62) {
    bump(0,&score);
  }
  if ((local_3d ^ local_40) == 99) {
    bump(0,&score);
  }
  if ((local_40 ^ local_42) == 0x52) {
    bump(0,&score);
  }
  if (local_4b == 0x31) {
    bump(0,&score);
  }
  if ((byte)(local_30 + local_4f) == 'g') {
    bump(0,&score);
  }
  if (local_4f == 0x7b) {
    bump(0,&score);
  }
  if (local_1d == 0x93) {
    bump(0,&score);
  }
  if ((local_4c ^ local_38) == 3) {
    bump(0,&score);
  }
  if (local_26 == 199) {
    bump(0,&score);
  }
  if (local_38 == 0x35) {
    bump(0,&score);
  }
  if (local_16 == 0x7d) {
    bump(0,&score);
  }
  if ((byte)(local_22 + local_2f) == 'G') {
    bump(0,&score);
  }
  if ((byte)(local_19 + local_41) == -0x6d) {
    bump(0,&score);
  }
  if ((local_54 ^ local_46) == 0x74) {
    bump(0,&score);
  }
  if ((local_4a ^ local_1b) == 0x16) {
    bump(0,&score);
  }
  if (local_23 == 0x31) {
    bump(0,&score);
  }
  if ((byte)(local_55 + local_16) == -0x33) {
    bump(0,&score);
  }
  if (local_19 == 0x32) {
    bump(0,&score);
  }
  if (local_1f == 99) {
    bump(0,&score);
  }
  if (local_4e == 0x4b) {
    bump(0,&score);
  }
  if ((local_38 ^ local_2d) == 0x57) {
    bump(0,&score);
  }
  if (local_1b == 0x39) {
    bump(0,&score);
  }
  if ((local_34 ^ local_29) == 0x56) {
    bump(0,&score);
  }
  if (local_44 == 0x96) {
    bump(0,&score);
  }
  if (local_42 == 0xab) {
    bump(0,&score);
  }
  if ((byte)(local_1a + local_22) == -0x51) {
    bump(0,&score);
  }
  if (local_40 == 0x7f) {
    bump(0,&score);
  }
  if ((local_32 ^ local_4a) == 0xd1) {
    bump(0,&score);
  }
  if (local_2d == 0x62) {
    bump(0,&score);
  }
  if ((local_43 ^ local_48) == 0x5e) {
    bump(0,&score);
  }
  if (local_4e == 0x16) {
    bump(0,&score);
  }
  if ((byte)(local_1f + local_4f) == -0x69) {
    bump(0,&score);
  }
  if (local_23 == 0x31) {
    bump(0,&score);
  }
  if (local_28 == 0x37) {
    bump(0,&score);
  }
  if ((byte)(local_42 + local_50) == 'h') {
    bump(0,&score);
  }
  if (local_51 == 0x1a) {
    bump(0,&score);
  }
  if (local_17 == 0x30) {
    bump(0,&score);
  }
  if ((local_49 ^ local_3d) == 4) {
    bump(0,&score);
  }
  if ((byte)(local_27 + local_35) == -0x6a) {
    bump(0,&score);
  }
  if (local_33 == 0x61) {
    bump(0,&score);
  }
  if (local_52 == 0x46) {
    bump(0,&score);
  }
  if ((byte)(local_4a + local_26) == -0x69) {
    bump(0,&score);
  }
  if (local_27 == 0x32) {
    bump(0,&score);
  }
  if (local_3c == 0x60) {
    bump(0,&score);
  }
  if (local_4c == 0x36) {
    bump(0,&score);
  }
  if (local_3b == 0x3a) {
    bump(0,&score);
  }
  if ((local_1e ^ local_2b) == 0xc) {
    bump(0,&score);
  }
  if ((local_33 ^ local_42) == 0x57) {
    bump(0,&score);
  }
  if (local_1d == 0x61) {
    bump(0,&score);
  }
  if ((local_2a ^ local_36) == 0x51) {
    bump(0,&score);
  }
  if (local_1e == 0x35) {
    bump(0,&score);
  }
  if (local_4c == 0xa9) {
    bump(0,&score);
  }
  if ((byte)(local_27 + local_52) == 'x') {
    bump(0,&score);
  }
  if (local_25 == 0x1f) {
    bump(0,&score);
  }
  if ((byte)(local_32 + local_3e) == -99) {
    bump(0,&score);
  }
  if (local_31 == 'm') {
    bump(0,&score);
  }
  if ((local_37 ^ local_39) == 6) {
    bump(0,&score);
  }
  if (local_20 == 0x30) {
    bump(0,&score);
  }
  if (local_41 == 0xf7) {
    bump(0,&score);
  }
  if (local_23 == 0x31) {
    bump(0,&score);
  }
  if ((byte)(local_19 + local_28) == 'i') {
    bump(0,&score);
  }
  if ((local_2c ^ local_49) == 5) {
    bump(0,&score);
  }
  if ((local_4c ^ local_2b) == 0x85) {
    bump(0,&score);
  }
  if (local_35 == 100) {
    bump(0,&score);
  }
  if (local_20 == 0x30) {
    bump(0,&score);
  }
  if ((byte)(local_2f + local_1e) == 'g') {
    bump(0,&score);
  }
  if (local_35 == local_48) {
    bump(&score);
  }
  if (local_31 == '2') {
    bump(0,&score);
  }
  if (local_3e == 0x9b) {
    bump(0,&score);
  }
  if (local_48 == 100) {
    bump(0,&score);
  }
  if (local_4d == 0x31) {
    bump(0,&score);
  }
  if (local_31 == '2') {
    bump(0,&score);
  }
  if (local_47 == 0xc3) {
    bump(0,&score);
  }
  if ((byte)(local_2c + local_40) == -0x69) {
    bump(0,&score);
  }
  if ((byte)(local_28 + local_30) == 'j') {
    bump(0,&score);
  }
  if (local_35 == 0x32) {
    bump(0,&score);
  }
  if (local_29 == 100) {
    bump(0,&score);
  }
  if (local_53 == 0x54) {
    bump(0,&score);
  }
  if ((local_32 ^ local_23) == 0x54) {
    bump(0,&score);
  }
  if (local_22 == 0x32) {
    bump(0,&score);
  }
  if (local_25 == 0x35) {
    bump(0,&score);
  }
  if (local_2c == 0x33) {
    bump(0,&score);
  }
  if (local_3a == 0x32) {
    bump(0,&score);
  }
  if ((byte)(local_24 + local_1a) == -0x69) {
    bump(0,&score);
  }
  if (local_31 == '2') {
    bump(0,&score);
  }
  if (local_3f == 0x61) {
    bump(0,&score);
  }
  if ((byte)(local_1e + local_51) == '\x12') {
    bump(0,&score);
  }
  if (local_27 == 0x9e) {
    bump(0,&score);
  }
  if ((local_3f ^ local_36) == 0x55) {
    bump(0,&score);
  }
  if (local_23 == 0x43) {
    bump(0,&score);
  }
  if (local_3e == 0x38) {
    bump(0,&score);
  }
  if (local_21 == 0xc) {
    bump(0,&score);
  }
  if (local_21 == 0x30) {
    bump(0,&score);
  }
  if (local_3f == 0x61) {
    bump(0,&score);
  }
  if (local_47 == 0x36) {
    bump(0,&score);
  }
  if (local_53 == 0x54) {
    bump(0,&score);
  }
  if ((local_4d ^ local_3f) == 0x50) {
    bump(0,&score);
  }
  if ((byte)(local_32 + local_55) == -0x59) {
    bump(0,&score);
  }
  if ((byte)(local_2e + local_53) == -0x39) {
    bump(0,&score);
  }
  if ((local_2c ^ local_4f) == 7) {
    bump(0,&score);
  }
  if ((byte)(local_34 + local_4a) == -0x5b) {
    bump(0,&score);
  }
  if (local_3c == 0x62) {
    bump(0,&score);
  }
  if (local_3b == 0x31) {
    bump(0,&score);
  }
  if ((byte)(local_41 + local_3a) == '#') {
    bump(0,&score);
  }
  if ((local_4f ^ local_32) == 0x9c) {
    bump(0,&score);
  }
  if ((local_47 ^ local_4a) == 4) {
    bump(0,&score);
  }
  if (local_2e == '4') {
    bump(0,&score);
  }
  if ((byte)(local_2d + local_36) == -0x6a) {
    bump(0,&score);
  }
  if (local_1c == 99) {
    bump(0,&score);
  }
  if (local_4e == 100) {
    bump(0,&score);
  }
  if (local_47 == 0x36) {
    bump(0,&score);
  }
  if (local_50 == 0x43) {
    bump(0,&score);
  }
  if ((local_3e ^ local_3f) == 0x59) {
    bump(0,&score);
  }
  if (local_40 == 100) {
    bump(0,&score);
  }
  if ((local_3f ^ local_29) == 5) {
    bump(0,&score);
  }
  if (local_20 == 0x30) {
    bump(0,&score);
  }
  if (local_36 == 0x34) {
    bump(0,&score);
  }
  if (local_3f == 0x61) {
    bump(0,&score);
  }
  if ((byte)(local_27 + local_4d) == 'z') {
    bump(0,&score);
  }
  if ((local_3c ^ local_52) == 0x24) {
    bump(0,&score);
  }
  if (local_2a == 0x65) {
    bump(0,&score);
  }
  if (local_29 == 0xf) {
    bump(0,&score);
  }
  if ((local_45 ^ local_40) == 0x57) {
    bump(0,&score);
  }
  if ((local_4c ^ local_17) == 6) {
    bump(0,&score);
  }
  if (local_3a == 0x32) {
    bump(0,&score);
  }
  if ((byte)(local_43 + local_1f) == -0x2f) {
    bump(0,&score);
  }
  if (local_35 == 100) {
    bump(0,&score);
  }
  if ((byte)(local_1c + local_43) == -0x39) {
    bump(0,&score);
  }
  if ((local_2a ^ local_35) == 1) {
    bump(0,&score);
  }
  if (local_44 == 0xa4) {
    bump(0,&score);
  }
  if ((local_4d ^ local_4c) == 7) {
    bump(0,&score);
  }
  if (local_2d == 0x62) {
    bump(0,&score);
  }
  if ((byte)(local_1d + local_51) == '\n') {
    bump(0,&score);
  }
  if ((byte)(local_40 + local_39) == -0x67) {
    bump(0,&score);
  }
  if (local_49 == 0x7c) {
    bump(0,&score);
  }
  if ((byte)(local_16 + local_43) == -0x1f) {
    bump(0,&score);
  }
  if (local_3a == 0x32) {
    bump(0,&score);
  }
  if (local_3e == 0x38) {
    bump(0,&score);
  }
  if ((byte)(local_29 + local_43) == -0x38) {
    bump(0,&score);
  }
  if ((byte)(local_4c + local_42) == 'l') {
    bump(0,&score);
  }
  if ((byte)(local_18 + local_4a) == -0x19) {
    bump(0,&score);
  }
  if (local_40 == 100) {
    bump(0,&score);
  }
  if ((byte)(local_1c + local_36) == -0x69) {
    bump(0,&score);
  }
  if ((local_39 ^ local_2d) == 0x57) {
    bump(0,&score);
  }
  if (local_28 == 0x37) {
    bump(0,&score);
  }
  if ((byte)(local_48 + local_26) == -0x37) {
    bump(0,&score);
  }
  if (local_43 == 100) {
    bump(0,&score);
  }
  if (local_46 == 0x37) {
    bump(0,&score);
  }
  if ((local_1b ^ local_45) == 10) {
    bump(0,&score);
  }
  if ((local_55 ^ local_40) == 0x34) {
    bump(0,&score);
  }
  if ((byte)(local_17 + local_24) == -0x6f) {
    bump(0,&score);
  }
  if (local_27 == 0x32) {
    bump(0,&score);
  }
  if ((byte)(local_1c + local_55) == -0x58) {
    bump(0,&score);
  }
  if (local_31 == '2') {
    bump(0,&score);
  }
  if (local_23 == 0x31) {
    bump(0,&score);
  }
  if (local_25 == 0x35) {
    bump(0,&score);
  }
  if (local_2b == 0x39) {
    bump(0,&score);
  }
  if ((byte)(local_18 + local_32) == -0x6b) {
    bump(0,&score);
  }
  if ((byte)(local_3a + local_54) == 'u') {
    bump(0,&score);
  }
  if (local_25 == 0x35) {
    bump(0,&score);
  }
  if ((local_32 ^ local_34) == 0x51) {
    bump(0,&score);
  }
  if ((local_38 ^ local_1c) == 0x56) {
    bump(0,&score);
  }
  if (local_3e == 0x4b) {
    bump(0,&score);
  }
  if ((byte)(local_36 + local_48) == -0x54) {
    bump(0,&score);
  }
  if (local_2e == 'J') {
    bump(0,&score);
  }
  if (local_2e == '4') {
    bump(0,&score);
  }
  if (local_34 == 0x73) {
    bump(0,&score);
  }
  if (local_4e == 100) {
    bump(0,&score);
  }
  if (local_55 == 0x50) {
    bump(0,&score);
  }
  if (local_3f == 0x61) {
    bump(0,&score);
  }
  if ((byte)(local_17 + local_1e) == 'e') {
    bump(0,&score);
  }
  if (local_21 == 0x30) {
    bump(0,&score);
  }
  if ((byte)(local_4e + local_3f) == -0x34) {
    bump(0,&score);
  }
  if ((local_3b ^ local_47) == 7) {
    bump(0,&score);
  }
  if (local_53 == 0x54) {
    bump(0,&score);
  }
  if (local_27 == 0x32) {
    bump(0,&score);
  }
  if (local_21 == 0x30) {
    bump(0,&score);
  }
  if ((local_1f ^ local_32) == 6) {
    bump(0,&score);
  }
  if ((local_36 ^ local_33) == 0x55) {
    bump(0,&score);
  }
  if (local_34 == 0x32) {
    bump(0,&score);
  }
  if ((byte)(local_2d + local_34) == -0x6c) {
    bump(0,&score);
  }
  if (local_4e == 100) {
    bump(0,&score);
  }
  if (local_46 == 0x37) {
    bump(0,&score);
  }
  if ((local_4b ^ local_2a) == 0x54) {
    bump(0,&score);
  }
  if (local_46 == 0x37) {
    bump(0,&score);
  }
  if ((byte)(local_38 + local_37) == 'h') {
    bump(0,&score);
  }
  if ((local_2a ^ local_48) == 1) {
    bump(0,&score);
  }
  if ((byte)(local_1b + local_3d) == -0x27) {
    bump(0,&score);
  }
  if ((byte)(local_44 + local_18) == 'i') {
    bump(0,&score);
  }
  if (local_2c == 0xa6) {
    bump(0,&score);
  }
  if ((local_1f ^ local_3d) == 0x51) {
    bump(0,&score);
  }
  if (local_17 == 0x30) {
    bump(0,&score);
  }
  if ((byte)(local_1c + local_30) == -0x6a) {
    bump(0,&score);
  }
  if ((local_18 ^ local_51) == 0x4b) {
    bump(0,&score);
  }
  if ((byte)(local_30 + local_21) == 'c') {
    bump(0,&score);
  }
  if ((local_40 ^ local_3b) == 0x3d) {
    bump(0,&score);
  }
  if (local_23 == 0xe9) {
    bump(0,&score);
  }
  if ((local_50 ^ local_38) == 7) {
    bump(0,&score);
  }
  if (local_36 == 0x34) {
    bump(0,&score);
  }
  if (local_20 == 1) {
    bump(0,&score);
  }
  if ((byte)(local_46 + local_4e) == -0x65) {
    bump(0,&score);
  }
  if (local_2c == 0x33) {
    bump(0,&score);
  }
  if ((byte)(local_32 + local_3a) == -0x69) {
    bump(0,&score);
  }
  if (local_2b == 0x39) {
    bump(0,&score);
  }
  if (local_3a == 0x32) {
    bump(0,&score);
  }
  if (local_26 == 0x65) {
    bump(0,&score);
  }
  if ((local_28 ^ local_37) == 4) {
    bump(0,&score);
  }
  if (local_37 == 0x33) {
    bump(0,&score);
  }
  if (local_3f == 0x61) {
    bump(0,&score);
  }
  if (local_24 == 0x61) {
    bump(0,&score);
  }
  if ((byte)(local_36 + local_40) == -0x68) {
    bump(0,&score);
  }
  if (local_3d == 0x32) {
    bump(0,&score);
  }
  if (local_46 == 0x37) {
    bump(0,&score);
  }
  if (local_32 == 0xcb) {
    bump(0,&score);
  }
  if ((byte)(local_51 + local_30) == -0x52) {
    bump(0,&score);
  }
  if (local_24 == 0x61) {
    bump(0,&score);
  }
  if ((local_4e ^ local_36) == 0x50) {
    bump(0,&score);
  }
  if ((byte)(local_46 + local_42) == 'm') {
    bump(0,&score);
  }
  if ((local_37 ^ local_3f) == 199) {
    bump(0,&score);
  }
  if ((local_45 ^ local_19) == 1) {
    bump(0,&score);
  }
  if (local_49 == 0x36) {
    bump(0,&score);
  }
  if (local_39 == 1) {
    bump(0,&score);
  }
  if ((byte)(local_29 + local_1b) == -99) {
    bump(0,&score);
  }
  if ((local_24 ^ local_30) == 0x52) {
    bump(0,&score);
  }
  if (local_4f == 0x34) {
    bump(0,&score);
  }
  if (local_2f == 0x32) {
    bump(0,&score);
  }
  if (local_17 == 0x30) {
    bump(0,&score);
  }
  if ((local_30 ^ local_40) == 0x57) {
    bump(0,&score);
  }
  if ((byte)(local_2d + local_50) == -0x6c) {
    bump(0,&score);
  }
  if ((byte)(local_4a + local_33) == -0x6d) {
    bump(0,&score);
  }
  if (local_2a == 0x99) {
    bump(0,&score);
  }
  if ((byte)(local_3f + local_3a) == -0x78) {
    bump(0,&score);
  }
  if (local_27 == local_2f) {
    bump(&score);
  }
  if ((local_25 ^ local_18) == 5) {
    bump(0,&score);
  }
  if (local_49 == 0x56) {
    bump(0,&score);
  }
  if ((local_29 ^ local_39) == 0x51) {
    bump(0,&score);
  }
  if (local_28 == 0x37) {
    bump(0,&score);
  }
  if ((local_30 ^ local_53) == 0x67) {
    bump(0,&score);
  }
  if ((local_1f ^ local_45) == 0x7b) {
    bump(0,&score);
  }
  if ((local_28 ^ local_43) == 0x91) {
    bump(0,&score);
  }
  if (local_43 == 100) {
    bump(0,&score);
  }
'''

def var_index(name: str) -> int:
    """
    Extracts the index (0..63) from "local_XX".
    Logic: index = 0x55 - int(suffix,16).
    Example: local_55 -> 0, local_54 -> 1, etc.
    """
    suffix = name.split('_')[1]
    offset_hex = int(suffix, 16)
    idx = 0x55 - offset_hex
    return idx

# Regex patterns to identify the constraints we handle:
pat_char = re.compile(r'\'(.)\'')  # Matches a character in single quotes

# -- local_XX == constant
pat_eq_const = re.compile(
    r'''
    if                   # the "if"
    \s*                  # optional spaces
    \(                   # opening parenthesis
    \s*\(*\s*           # optional parentheses and spaces
    local_([0-9A-Fa-f]+) # captures the hexadecimal (e.g., 3a, 4b, etc.)
    \s*\)*\s*           # optional parentheses/spaces
    ==                  # equality operator
    \s*\(*\s*           # optional parentheses/spaces
    (                   # captures the constant in the following group
      0x[0-9A-Fa-f]+    # hexadecimal form (0x..)
      | \d+             # decimal form
      | \'.\'           # or a character in single quotes, e.g., 'a'
    )
    \s*\)*\s*           # optional parentheses/spaces
    \)                   # closing parenthesis of the if
    ''',
    re.VERBOSE
)

# -- local_XX == local_YY
pat_eq_var = re.compile(
    r'''
    if
    \s*
    \(
    \s*\(*\s*
    local_([0-9A-Fa-f]+)
    \s*\)*\s*
    ==
    \s*\(*\s*
    local_([0-9A-Fa-f]+)
    \s*\)*\s*
    \)
    ''',
    re.VERBOSE
)

# -- (local_XX ^ local_YY) == constant
pat_xor_const = re.compile(
    r'''
    if
    \s*
    \(
    \s*\(*\s*
    \(?
    \s*local_([0-9A-Fa-f]+)\s*
    \^
    \s*local_([0-9A-Fa-f]+)\s*
    \)?
    \s*\)*\s*
    ==
    \s*\(*\s*
    (0x[0-9A-Fa-f]+|\d+)
    \s*\)*\s*
    \)
    ''',
    re.VERBOSE
)

# -- (byte)(local_XX + local_YY) == constant
pat_sum_const = re.compile(
    r'''
    if
    \s*
    \(
    \s*\(byte\)\(
        \s*\(*local_([0-9A-Fa-f]+)\)*\s*
        \+
        \s*\(*local_([0-9A-Fa-f]+)\)*\s*
    \)
    \s*
    ==
    \s*\(*\s*
    (-?0x[0-9A-Fa-f]+|\'.\'|\d+)
    \s*\)*\s*
    \)
    ''',
    re.VERBOSE
)

constraints = []

def parse_constraints(text: str):
    """Extracts constraints in the form (ctype, idxA, idxB, [val])"""
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line.startswith('if'):
            continue

        # 1) local_XX == local_YY
        m = pat_eq_var.search(line)
        if m:
            idxA = var_index("local_" + m.group(1))
            idxB = var_index("local_" + m.group(2))
            constraints.append(("==var", idxA, idxB))
            continue

        # 2) local_XX == constant
        m = pat_eq_const.search(line)
        if m:
            idxA = var_index("local_" + m.group(1))
            val_str = m.group(2)
            # Parse the value
            mc = pat_char.match(val_str)
            if mc:
                val = ord(mc.group(1))
            elif val_str.startswith('0x') or val_str.startswith('0X'):
                val = int(val_str,16) & 0xFF
            else:
                val = int(val_str) & 0xFF
            constraints.append(("==const", idxA, val))
            continue

        # 3) (local_X ^ local_Y) == constant
        m = pat_xor_const.search(line)
        if m:
            idxA = var_index("local_" + m.group(1))
            idxB = var_index("local_" + m.group(2))
            val  = int(m.group(3),16) & 0xFF
            constraints.append(("xor", idxA, idxB, val))
            continue

        # 4) ( (local_X + local_Y) & 0xFF ) == constant
        m = pat_sum_const.search(line)
        if m:
            idxA = var_index("local_" + m.group(1))
            idxB = var_index("local_" + m.group(2))
            val_str = m.group(3)
            mc = pat_char.match(val_str)
            if mc:
                val = ord(mc.group(1))
            elif val_str.startswith('-0x'):
                negative_val = int(val_str,16)
                val = (negative_val) & 0xFF
            else:
                val = int(val_str, 0) & 0xFF
            constraints.append(("sum", idxA, idxB, val))
            continue

# Fill "constraints"
parse_constraints(constraints_text)

print(f"Extracted {len(constraints)} constraints.")

# 64 variables (8 bits each)
vars_z3 = [BitVec(f'v{i}', 8) for i in range(64)]

opt = Optimize()
opt.add(vars_z3[0] == ord('P'))
opt.add(vars_z3[1] == ord('C'))
opt.add(vars_z3[2] == ord('T'))
opt.add(vars_z3[3] == ord('F'))
opt.add(vars_z3[4] == ord('{'))
set_param('smt.phase_selection', 5)
set_param('smt.arith.random_initial_value', True)
opt.set(timeout=1800000)

def constraint_to_z3expr(c):
    """Transforms a tuple (ctype, i, [j], [val]) into a Z3 expression."""
    ctype = c[0]
    
    if ctype == "==const":
        # c = ("==const", idx, val)
        idx, val = c[1], c[2]
        return (vars_z3[idx] == val)
    
    elif ctype == "==var":
        # c = ("==var", idxA, idxB)
        A, B = c[1], c[2]
        return (vars_z3[A] == vars_z3[B])
    
    elif ctype == "xor":
        # c = ("xor", idxA, idxB, val)
        A, B, v = c[1], c[2], c[3]
        return ((vars_z3[A] ^ vars_z3[B]) == v)
    
    elif ctype == "sum":
        # c = ("sum", idxA, idxB, val)
        A, B, v = c[1], c[2], c[3]
        # We want (vars_z3[A] + vars_z3[B]) & 0xFF == v
        return (((vars_z3[A] + vars_z3[B]) & 0xFF) == v)
    
    else:
        # Unexpected case
        return None

# Add each constraint as "soft" so Z3 maximizes the number of satisfied constraints
for c in constraints:
    expr = constraint_to_z3expr(c)
    if expr is not None:
        # Weight 1 for each constraint
        opt.add_soft(expr, weight=1)

res = opt.check()
if res == sat:
    # Retrieve the model
    model = opt.model()

    # Build the solution (64 bytes) from the model
    solution = [0]*64
    for i in range(64):
        val = model[vars_z3[i]]
        if val is None:
            solution[i] = 0
        else:
            solution[i] = val.as_long() & 0xFF

    # Count how many constraints are satisfied
    def check_constraint(c, sol):
        ctype = c[0]
        if ctype == "==const":
            idx, v = c[1], c[2]
            return (sol[idx] == v)
        elif ctype == "==var":
            A, B = c[1], c[2]
            return (sol[A] == sol[B])
        elif ctype == "xor":
            A, B, v = c[1], c[2], c[3]
            return ((sol[A] ^ sol[B]) & 0xFF) == v
        elif ctype == "sum":
            A, B, v = c[1], c[2], c[3]
            return (((sol[A] + sol[B]) & 0xFF) == v)
        return False

    score = sum(check_constraint(c, solution) for c in constraints)

    print(f"[+] Max-SAT => Satisfied {score} constraints out of {len(constraints)}!")
    print("[+] Proposed solution (64 bytes, in hex):")
    print(" ".join(f"{x:02x}" for x in solution))

    # ASCII display
    ascii_str = "".join(chr(x) for x in solution)
    print("[+] As ASCII: ")
    print(ascii_str)

else:
    print("[!] No satisfactory solution (unsat).")
