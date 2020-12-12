  $(document).ready(function(){
     
   $("#about-btn").click(function(){
      $("#imgplaca").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","block");
          });
        }  
      });
       $("#imgtarjeta").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
        $("#imgciv").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
         $("#imgname").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });

    });

    $("#ver-civ").click(function(){
      $("#imgciv").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","block");
          });
        }  
      });
       $("#imgtarjeta").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
        $("#imgplaca").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
         $("#imgname").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });

    });

     $("#ver-name").click(function(){
      $("#imgname").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","block");
          });
        }  
      });
       $("#imgtarjeta").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
        $("#imgciv").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
         $("#imgplaca").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });

    });

      $("#radio1").change(function () {	 
		$("#placa").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","block");
          });
        } 
     	 });

		$("#civ").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
     	 });

		$("#name").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
     	 });
		$("#imgplaca").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","block");
          });
        }  
      });
       $("#imgtarjeta").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
        $("#imgciv").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
         $("#imgname").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });


	  });

	  $("#radio2").change(function () {	 
		$("#placa").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('show',function() {
           $(this).css("display","none");
          });
        } 
     	 });

		$("#civ").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('show',function() {
           $(this).css("display","block");
          });
        } 
     	 });

		$("#name").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
     	 });

		 $("#imgciv").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","block");
          });
        }  
      });
       $("#imgtarjeta").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
        $("#imgplaca").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
         $("#imgname").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });


	  });


	   $("#radio3").change(function () {	 
		$("#placa").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('show',function() {
           $(this).css("display","none");
          });
        } 
     	 });

		$("#name").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('show',function() {
           $(this).css("display","block");
          });
        } 
     	 });

		$("#civ").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
     	 });

		 $("#imgname").each(function() {
        displaying = $(this).css("display");
        if(displaying == "none") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","block");
          });
        }  
      });
       $("#imgtarjeta").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
        $("#imgciv").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });
         $("#imgplaca").each(function() {
        displaying = $(this).css("display");
        if(displaying == "block") {
          $(this).fadeOut('slow',function() {
           $(this).css("display","none");
          });
        } 
      });


	  });


	  

 
  });
