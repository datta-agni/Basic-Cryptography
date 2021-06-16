# Substitution Cipher

## The Reverse Cipher

#### 1. Introduction

-  The reverse cipher encrypts a message by printing it in reverse. Example AKHILESH encrypt to HSELIHKA.
- Reverse cipher is very weak in cipher.

#### 2. Algorithm
- The process of encryptions and decryption is same.
- When using the Reverse Cipher, there is only 1 way to complete the transposition, so there is only 1 key for enciphering and deciphering messages.

#### 3. Explanation
- Plain text stored in variable and then variable is revered.

#####   Programs

- [Python](#Reverse_Cipher.py)
- [CPP](#Reverse_Cipher.cpp)


## Caesar Cipher

#### 1.Introduction
- Simplest and most well-know encryption techniques.
- Provide minimum security to information.
- Simple structure usage.
- Frequency of the letter pattern provides a big clue in decrypt the entire message.

#### 2.Algorithm
- Each letter of plain text is replaced by the letter with some fixed number of positions.
- Formula of encryption  

$$
C_i = (T_i + k)(mod m)
$$



***Ci* – i-th character of the closed text**

***Ti* – i-th character of the open text**

***k* – shift**

***m* – length of the alphabet**

- The process of decryption

$$
T_i = (C_i - k)(mod m)
$$

#### 3.Explation
- Plain text is transform according to the rule depending on the procedure of encryption and decryption of text.

#####   Programs
- [Python](#Ceasar_Cipher.py)
- [CPP](#Ceasar_Cipher.cpp)


## Rail Fence Cipher
#### 1.Introductions
- Called as zigzag cipher
- Works by writing your message on alternate lines across the page.
For Example lets consider plaintext "**AKHILESH**"
To encode this message

| A    |      |   H   |      |   L   |      |   S   |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      | **K** |      |  **I**  |      |   **E**   |      |  **H**  |

Then read off by writing the top row first, followed by thee bottom row:

ciphertext: **AHLSKIEH**

#### 2.Algorithm
Incomplete


#### 3.Explaination
- Take an integer key as an input and create a matrix with:
    - number of rows = key
    - number of columns = size of message (text that is to be encrypted)
- reverse the matrix in row wise manner and if the element is not equal to “*“  ,then store it in a string.

#### 4.Extension 
- Rail Fence Ciphers may have more rails.

- Number of lines used in a rail fence cipher is called the **KEY**.
  Example 
  Plain text = **HIAGNIHOWAREYOU**

  Key = 3

  | H    |       |       |       | N   |       |       |       | W    |       |       |       | Y    |       |       |
  | ---- | :---: | ----- | ----- | ---- | ----- | ----- | ----- | ---- | ----- | ----- | ----- | ---- | ----- | ----- |
  |      | **I** |       | **G** |      | **I** |       | **O** |      | **A** |       | **E** |      | **O** |       |
  |      |       | **A** |       |      |       | **H** |       |      |       | **R** |       |      |       | **U** |

  Ciphertext = **HNWTIGIOAEOUAHRU**

#####   Programs
- [Python](#Rail_Fence_Cipher.py)
- [CPP](#Rail_Fence_Cipher.cpp)