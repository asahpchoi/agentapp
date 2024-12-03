��B u s i n e s s   R o l e   G e n e r a t o r   a n d   D i s c u s s i o n   P l a t f o r m 
 
 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
 
 
 
 A   F a s t A P I - b a s e d   w e b   a p p l i c a t i o n   t h a t   g e n e r a t e s   b u s i n e s s   r o l e s   u s i n g   O p e n A I ' s   G P T   m o d e l   a n d   f a c i l i t a t e s   b u s i n e s s   p l a n   d i s c u s s i o n s . 
 
 
 
 P r o j e c t   S t r u c t u r e 
 
 - - - - - - - - - - - - - - - 
 
 / 
 
 % % %  a p i . p y                             #   M a i n   F a s t A P I   a p p l i c a t i o n 
 
 % % %  s t a t i c /                         #   S t a t i c   f i l e s   d i r e c t o r y 
 
 %      % % %  i n d e x . h t m l           #   M a i n   w e b   i n t e r f a c e 
 
 %      % % %  s t y l e s . c s s           #   C S S   s t y l e s 
 
 %      % % %  s c r i p t s . j s           #   J a v a S c r i p t   f u n c t i o n a l i t y 
 
 % % %  r e q u i r e m e n t s . t x t       #   P y t h o n   d e p e n d e n c i e s 
 
 % % %  . e n v                             #   E n v i r o n m e n t   v a r i a b l e s 
 
 
 
 F e a t u r e s 
 
 - - - - - - - - 
 
 1 .   R o l e   G e n e r a t i o n 
 
       -   G e n e r a t e   1 - 5   b u s i n e s s   r o l e s   b a s e d   o n   a   g i v e n   t o p i c 
 
       -   E a c h   r o l e   i n c l u d e s   a   t i t l e ,   d e s c r i p t i o n ,   a n d   i n s t r u c t i o n 
 
       -   U s e s   O p e n A I ' s   G P T   m o d e l   f o r   g e n e r a t i o n 
 
 
 
 2 .   R o l e   M a n a g e m e n t 
 
       -   S a v e   g e n e r a t e d   r o l e s   t o   S u p a b a s e   d a t a b a s e 
 
       -   V i e w   s a v e d   r o l e s 
 
       -   S t a r t   d i s c u s s i o n s   w i t h   g e n e r a t e d   r o l e s 
 
 
 
 3 .   C h a t   I n t e r f a c e 
 
       -   I n t e r a c t   w i t h   g e n e r a t e d   r o l e s 
 
       -   D i s c u s s   b u s i n e s s   s t r a t e g i e s 
 
       -   V i e w   c h a t   h i s t o r y 
 
 
 
 A P I   E n d p o i n t s 
 
 - - - - - - - - - - - - 
 
 1 .   B a s i c   U t i l i t y 
 
       -   G E T   / e c h o / { m e s s a g e }           :   E c h o   t e s t   e n d p o i n t 
 
       -   G E T   / c h a t / { m e s s a g e }           :   C h a t   w i t h   a g e n t s 
 
       -   G E T   / c o d e / { p r o m p t }             :   G e n e r a t e   c o d e 
 
 
 
 2 .   D a t a b a s e   O p e r a t i o n s 
 
       -   P O S T   / m e s s a g e s                   :   S a v e   c h a t   m e s s a g e s 
 
       -   P O S T   / s a v e _ r o l e s             :   S a v e   g e n e r a t e d   r o l e s 
 
 
 
 3 .   R o l e   G e n e r a t i o n   a n d   D i s c u s s i o n 
 
       -   P O S T   / g e n e r a t e _ r o l e s     :   G e n e r a t e   b u s i n e s s   r o l e s 
 
       -   P O S T   / s t a r t _ t a l k           :   S t a r t   a   d i s c u s s i o n 
 
 
 
 S e t u p 
 
 - - - - - 
 
 1 .   E n v i r o n m e n t   V a r i a b l e s   R e q u i r e d : 
 
       -   S U P A B A S E _ U R L                   :   S u p a b a s e   p r o j e c t   U R L 
 
       -   S U P A B A S E _ K E Y                   :   S u p a b a s e   A P I   k e y 
 
       -   A Z U R E _ A P I _ K E Y                 :   A z u r e   O p e n A I   A P I   k e y 
 
 
 
 2 .   I n s t a l l   D e p e n d e n c i e s : 
 
       p i p   i n s t a l l   - r   r e q u i r e m e n t s . t x t 
 
 
 
 3 .   R u n   t h e   A p p l i c a t i o n : 
 
       u v i c o r n   a p i : a p p   - - r e l o a d 
 
 
 
 U s a g e 
 
 - - - - - 
 
 1 .   G e n e r a t e   R o l e s : 
 
       -   E n t e r   a   b u s i n e s s   t o p i c 
 
       -   S p e c i f y   n u m b e r   o f   r o l e s   ( 1 - 5 ) 
 
       -   C l i c k   " G e n e r a t e   R o l e s " 
 
 
 
 2 .   S a v e   R o l e s : 
 
       -   R e v i e w   g e n e r a t e d   r o l e s 
 
       -   C l i c k   " S a v e   R o l e s "   t o   s t o r e   i n   d a t a b a s e 
 
 
 
 3 .   S t a r t   D i s c u s s i o n : 
 
       -   C l i c k   " S t a r t   D i s c u s s i o n "   w i t h   s a v e d   r o l e s 
 
       -   E n t e r   m e s s a g e s   t o   i n t e r a c t   w i t h   r o l e s 
 
       -   V i e w   r e s p o n s e s   i n   c h a t   s e c t i o n 
 
 
 
 T e c h n i c a l   D e t a i l s 
 
 - - - - - - - - - - - - - - - 
 
 1 .   F r o n t e n d : 
 
       -   H T M L 5 ,   C S S 3 ,   J a v a S c r i p t 
 
       -   F e t c h   A P I   f o r   b a c k e n d   c o m m u n i c a t i o n 
 
       -   D y n a m i c   c o n t e n t   r e n d e r i n g 
 
 
 
 2 .   B a c k e n d : 
 
       -   F a s t A P I   f r a m e w o r k 
 
       -   P y d a n t i c   f o r   d a t a   v a l i d a t i o n 
 
       -   O p e n A I   i n t e g r a t i o n   f o r   r o l e   g e n e r a t i o n 
 
       -   S u p a b a s e   f o r   d a t a   s t o r a g e 
 
 
 
 3 .   D a t a   M o d e l s : 
 
       -   A g e n t R o l e :   t i t l e ,   d e s c r i p t i o n ,   i n s t r u c t i o n 
 
       -   T o p i c R e q u e s t :   t o p i c ,   n u m R o l e s 
 
       -   S a v e R o l e s R e q u e s t :   t o p i c ,   r o l e s [ ] 
 
       -   M e s s a g e :   c o n t e n t 
 
 
 
 E r r o r   H a n d l i n g 
 
 - - - - - - - - - - - - - 
 
 -   I n p u t   v a l i d a t i o n   f o r   a l l   e n d p o i n t s 
 
 -   D e t a i l e d   e r r o r   l o g g i n g 
 
 -   U s e r - f r i e n d l y   e r r o r   m e s s a g e s 
 
 -   E x c e p t i o n   h a n d l i n g   f o r   A P I   c a l l s 
 
 
 
 D e p e n d e n c i e s 
 
 - - - - - - - - - - - 
 
 -   f a s t a p i 
 
 -   u v i c o r n 
 
 -   o p e n a i 
 
 -   s u p a b a s e 
 
 -   p y t h o n - d o t e n v 
 
 -   p y d a n t i c 
 
 
 
 N o t e :   S e e   r e q u i r e m e n t s . t x t   f o r   c o m p l e t e   l i s t   w i t h   v e r s i o n s . 
 
 