<?
include 'config/config.php';
include TVL_ROOT_DIR_PATH.'connection/connect.php';
include TVL_ROOT_DIR_PATH.'classes/site/product_functions.class.php';
$tvl_objCon	=	new dbConnect();
$objProduct	=	new ProductFunctions();
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
		<meta name="description" content="Click and Search the best phones on clicknsearch.in. Compare phones, reviews, and specs of the newest phones Android, Apple,Windows phones etc.">
		<meta name="keywords" content="clicknsearch.in,smartphones,smart phones,budget phones,android mobiles,windows phones,mobile phone list,phone list,mobile list,nokia phones,samsung phones,mobile,phones,search mobile,search phones,Smartphones, Smartphone Reviews, Smartphone Specifications, Smartphone Comparison, Best Smartphones, smart phones,search mobile phones,buy mobile,buy phones,buy mobile phones,best mobile phones">
        <meta property="og:description" content="Click and Search the best phones on clicknsearch.i. Compare phones, reviews, and specs of the newest phones Android, Apple,Windows phones etc.
" />
		<meta name="author" content="<? echo TVL_SITE_AUTH?>">
		<title><? echo TVL_SITE_AUTH?> </title>
 
		<!-- BOOTSTRAP CSS (REQUIRED ALL PAGE)-->
		<link href="<? echo TVL_ROOT_ASSETS_PATH?>assets/css/bootstrap.min.css" rel="stylesheet">
		
        
        <link href="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/owl-carousel/owl.carousel.min.css" rel="stylesheet">
		<link href="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/owl-carousel/owl.theme.min.css" rel="stylesheet">
		<link href="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/owl-carousel/owl.transitions.min.css" rel="stylesheet">
        
        
		<!-- MAIN CSS (REQUIRED ALL PAGE)-->
		<link href="<? echo TVL_ROOT_HTTP_PATH ?>assets/plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet">
		<link href="<? echo TVL_ROOT_ASSETS_PATH?>assets/css/style.css" rel="stylesheet">
		<link href="<? echo TVL_ROOT_ASSETS_PATH?>assets/css/style-responsive.css" rel="stylesheet">
 		<link href="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/slider/slider.min.css" rel="stylesheet">
		<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!--[if lt IE 9]>
		<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
		<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
		<![endif]-->
        <style>.tooltip-inner1{font-weight:bold; font-size:18px}</style>
	</head>
 
	<body class="tooltips">
		
			
		
		<!--
		===========================================================
		BEGIN PAGE
		===========================================================
		-->
		<div class="wrapper">
			<!-- BEGIN TOP NAV -->
			<? include 'mobiles/topnav.php'?>
			<!-- END TOP NAV -->
			<? include 'mobiles/menu.php'?>
						
			<!-- BEGIN PAGE CONTENT -->
			<div class="page-content-home">
				
				
				<div class="container-fluid">
					
				<p></p>
					<div class="the-box transparent full search-page">
						<div class="the-box no-margin no-border bg-success" id="search-heading">
							<div class="text-center">
                            
							<h1>LETS CLICK AND SEARCH A MOBILE PHONE</h1>
							</div>
                           <form role="form" action="<? echo TVL_ROOT_HTTP_PATH_MOBILES; ?>product.php">
								<div class="form-group has-feedback lg no-label"> 
								 <center>
                                             <div style="width:40%">
                                <!-- /.text-center -->
								<div class="text-center">                         
                                      <!--Slider-->
                                        <div class="text-center">                                  
                                             <input type="text" class="span2" value="" data-slider-min="500" data-slider-max="50000" data-slider-step="5" data-slider-value="[5000,15000]" id="sl2" > 
                                            <input type="hidden" name="p" value="f"/>                             
                                          <!--slider ends-->
                                        </div>
                                    </div><!-- /.text-center --> 
                                    </div>
                                    </center>                                
								</div>
                                
                                
                                <br clear="all"/> 
                                      <center>
                                             <div style="width:40%">
                                                <select name="Os"  class="form-control" tabindex="2">
                                                    <option value="">OS</option>
                                                    <option value="ANDROID">ANDROID</option>
                                                    <option value="BLACKBERRY">BLACKBERRY</option>
                                                    <option value="WINDOWS">WINDOWS</option>
                                                    <option value="IOS">APPLE IOS</option>
                                                </select> 
                                             </div>  
                                      </center>      
                                <br clear="all"/>       
                                <!-- /.text-center -->
								<div class="text-center">
									<button class="btn btn-warning"><i class="fa fa-globe"></i> Search</button>
								</div><!-- /.text-center -->
							</form>
						</div><!-- /.the-box full -->
                        
                     <!-- BEGIN CAROUSEL ITEM -->
					<div class="the-box no-border">
					<h4 class="small-heading more-margin-bottom text-center">LATEST MOBILES</h4>
						<div id="store-item-carousel-1" class="owl-carousel shop-carousel">
							
                           <? $qry="SELECT name, price FROM mobiles WHERE live=1 AND dc=0 ";
			 print_r($objProduct->setRecentWidget($qry,15))?>
                            
                            
						</div><!-- /#store-item-carousel-1 -->
					</div><!-- /.the-box .no-border -->
					<!-- END CAROUSEL ITEM -->
                    
                   
                    
                    
                       
					</div><!-- /.the-box full -->
					
				
				</div><!-- /.container-fluid -->
				
				
				
				<!-- BEGIN FOOTER -->
			<? include 'mobiles/footer.php'?>
				<!-- END FOOTER -->
				
				
			</div><!-- /.page-content -->
		</div><!-- /.wrapper -->
		<!-- END PAGE CONTENT -->
        
        <script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/js/jquery.min.js"></script>
		<script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/js/bootstrap.min.js"></script>
		<script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/retina/retina.min.js"></script>
		<script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/nicescroll/jquery.nicescroll.js"></script>
		<script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/slimscroll/jquery.slimscroll.min.js"></script>
		<script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/backstretch/jquery.backstretch.min.js"></script>
        <script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/slider/bootstrap-slider.js"></script>
          <script language="javascript" type="text/javascript" src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/autosuggest/jquery.coolautosuggest.js"></script>
		<script language="javascript" type="text/javascript" src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/autosuggest/jquery.coolfieldset.js"></script>
        
         <script>
		 $("#search").coolautosuggest({
						url:"http://clicknsearch.in/mobiles/autosuggest.php?chars=",
						 onSelected:function(result){var str=result.data;str=str.replace(/\s+/g, '-');window.location.href = "../mobiles/phone-" +str;}
					});
					</script>
        
        <script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/plugins/owl-carousel/owl.carousel.min.js"></script>
        <!-- MAIN APPS JS -->
		<script src="<? echo TVL_ROOT_ASSETS_PATH?>assets/js/apps.js"></script>

</body>
</html>