pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install pymongo==3.2.0 --user
                ./test/unit/mongo_class/fetch_cmd_line.py
                ./test/unit/mongo_class/fetch_db_info.py
                ./test/unit/mongo_class/fetch_ismaster.py
                ./test/unit/mongo_class/Coll_coll_dst.py
                ./test/unit/mongo_class/Coll_coll_find.py
                ./test/unit/mongo_class/Coll_coll_find1.py
                ./test/unit/mongo_class/Coll_coll_options.py
                ./test/unit/mongo_class/Coll_connect.py
                ./test/unit/mongo_class/Coll_init.py
                ./test/unit/mongo_class/Coll_ins_doc.py
                ./test/unit/mongo_class/DB_chg_db.py
                ./test/unit/mongo_class/DB_connect.py
                ./test/unit/mongo_class/DB_db_cmd.py
                ./test/unit/mongo_class/DB_db_connect.py
                ./test/unit/mongo_class/DB_get_tbl_list.py
                ./test/unit/mongo_class/DB_init.py
                ./test/unit/mongo_class/DB_isvalid_tbl.py
                ./test/unit/mongo_class/DB_validate_tbl.py
                ./test/unit/mongo_class/MasterRep_connect.py
                ./test/unit/mongo_class/MasterRep_init.py
                ./test/unit/mongo_class/RepSetColl_coll_cnt.py
                ./test/unit/mongo_class/RepSetColl_coll_del_many.py
                ./test/unit/mongo_class/RepSetColl_connect.py
                ./test/unit/mongo_class/RepSetColl_init.py
                ./test/unit/mongo_class/RepSetColl_ins_doc.py
                ./test/unit/mongo_class/RepSet_connect.py
                ./test/unit/mongo_class/RepSet_init.py
                ./test/unit/mongo_class/Rep_fetch_nodes.py
                ./test/unit/mongo_class/Rep_init.py
                ./test/unit/mongo_class/Server_connect.py
                ./test/unit/mongo_class/Server_disconnect.py
                ./test/unit/mongo_class/Server_fetch_adr.py
                ./test/unit/mongo_class/Server_fetch_dbs.py
                ./test/unit/mongo_class/Server_fetch_svr_info.py
                ./test/unit/mongo_class/Server_init.py
                ./test/unit/mongo_class/Server_is_locked.py
                ./test/unit/mongo_class/Server_is_primary.py
                ./test/unit/mongo_class/Server_lock_db.py
                ./test/unit/mongo_class/Server_unlock_db.py
                ./test/unit/mongo_class/Server_upd_server_attr.py
                ./test/unit/mongo_class/Server_upd_srv_stat.py
                ./test/unit/mongo_class/SlaveRep_connect.py
                ./test/unit/mongo_class/SlaveRep_init.py
                ./test/unit/mongo_libs/create_cmd.py
                ./test/unit/mongo_libs/create_instance.py
                ./test/unit/mongo_libs/create_slv_array.py
                ./test/unit/mongo_libs/crt_base_cmd.py
                ./test/unit/mongo_libs/crt_coll_inst.py
                ./test/unit/mongo_libs/ins_doc.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/mongo-lib/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
