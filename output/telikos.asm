L0:
b(jump) 24
L1: 
sw ra,(sp) 
L2: 
lw t1,-12(sp) 
li t2,1
ble,t1,t2,4
L3: 
b(jump) 6
L4: 
lw t1,-12(sp) 
lw t0,-8(sp) 
sw t1,(t0) 
lw ra,(sp) 
jr ra 
L5: 
b(jump) 16
L6: 
lw t1,-12(sp) 
li t2,1
sub t1,t1,t2 
L7: 
addi fp,sp,framelength 
sw t0,-36(fp) 
L8: 
addi fp,sp,framelength 
addi t0,sp,-20
sw t0,-8(fp) 
L9: 
lw t0,-4(sp)
sw t0,-4(fp)
addi sp,sp,36
jal _
addi sp,sp,36
L10: 
lw t1,-12(sp) 
li t2,2
sub t1,t1,t2 
L11: 
addi fp,sp,framelength 
sw t0,-52(fp) 
L12: 
addi fp,sp,framelength 
addi t0,sp,-28
sw t0,-8(fp) 
L13: 
lw t0,-4(sp)
sw t0,-4(fp)
addi sp,sp,36
jal _
addi sp,sp,36
L14: 
add t1,t1,t2 
L15: 
lw t0,-8(sp) 
sw t1,(t0) 
lw ra,(sp) 
jr ra 
L16: 
lw ra,(sp) 
jr ra 
L17: 
sw ra,(sp) 
L18: 
li a7,5 
ecall 
L19: 
addi fp,sp,framelength 
lw t0,-12(sp) 
sw t0,-20(fp) 
L20: 
addi fp,sp,framelength 
addi t0,sp,-16
sw t0,-8(fp) 
L21: 
sw sp,-4(fp)
addi sp,sp,36
jal _
addi sp,sp,36
L22: 
li a7,1 
ecall 
la a0,str_nl 
li a7,4 
ecall 
L23: 
lw ra,(sp) 
jr ra 
L24: 
addi sp,sp,12
mv gp,sp 
L25: 
sw sp,-4(fp)
addi sp,sp,20
jal _
addi sp,sp,20
L26: 
li a0,0 
li a7,93 
ecall 
L27: 
