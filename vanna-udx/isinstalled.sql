-- Installation verification script: make more specific pre-release, check the installed functions 

SELECT (COUNT(0) > 5) as VannaUdxInstalled
FROM user_libraries 
INNER JOIN user_library_manifest ON user_libraries.lib_name = user_library_manifest.lib_name
WHERE user_library_manifest.lib_name = 'VannaPyScalarFunctions';
