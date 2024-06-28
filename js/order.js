   let l = document.getElementById("l")
   let m = document.getElementById("m")
   let s = document.getElementById("s")
   let xl = document.getElementById("xl")
   let xxl = document.getElementById("xxl")
   let xxxl = document.getElementById("xxxl")
   let p_size = document.getElementById("p_size")
   

   
   const stt = "0px solid black"
   
   let sub = document.getElementById("sub")
   let add = document.getElementById("add")
   let num = document.getElementById("num")
   
   
   sub.onclick = function(){
   num.value--
   }
   add.onclick = function(){
   num.value++
   }
   
   l.onclick = function(){
    p_size.value = l.innerHTML
    l.style.borderBottom=stt
    
   }
   
   m.onclick = function(){
   p_size.value = m.innerHTML
   m.style.borderBottom=stt
   }
   
   s.onclick = function(){
   p_size.value = s.innerHTML
   s.style.borderBottom=stt
   }
   
   xl.onclick = function(){
   p_size.value = xl.innerHTML
   xl.style.borderBottom=stt
   }
   
   xxl.onclick = function(){
   p_size.value = xxl.innerHTML
   xxl.style.borderBottom=stt
   }
   
   xxxl.onclick = function(){
   p_size.value = xxxl.innerHTML
   xxxl.style.borderBottom=stt
   }
   
    
    