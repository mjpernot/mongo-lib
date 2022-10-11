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
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install pymongo==3.8.0 --user
                pip2 install psutil==5.4.3 --user
                /usr/bin/python ./test/unit/mongo_class/fetch_cmd_line.py
                /usr/bin/python ./test/unit/mongo_class/fetch_db_info.py
                /usr/bin/python ./test/unit/mongo_class/fetch_ismaster.py
                /usr/bin/python ./test/unit/mongo_class/coll_coll_cnt.py
                /usr/bin/python ./test/unit/mongo_class/coll_coll_dst.py
                /usr/bin/python ./test/unit/mongo_class/coll_coll_find.py
                /usr/bin/python ./test/unit/mongo_class/coll_coll_find1.py
                /usr/bin/python ./test/unit/mongo_class/coll_coll_options.py
                /usr/bin/python ./test/unit/mongo_class/coll_connect.py
                /usr/bin/python ./test/unit/mongo_class/coll_init.py
                /usr/bin/python ./test/unit/mongo_class/coll_ins_doc.py
                /usr/bin/python ./test/unit/mongo_class/db_chg_db.py
                /usr/bin/python ./test/unit/mongo_class/db_connect.py
                /usr/bin/python ./test/unit/mongo_class/db_db_cmd.py
                /usr/bin/python ./test/unit/mongo_class/db_db_connect.py
                /usr/bin/python ./test/unit/mongo_class/db_get_tbl_list.py
                /usr/bin/python ./test/unit/mongo_class/db_init.py
                /usr/bin/python ./test/unit/mongo_class/db_validate_tbl.py
                /usr/bin/python ./test/unit/mongo_class/masterrep_connect.py
                /usr/bin/python ./test/unit/mongo_class/masterrep_init.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_coll_cnt.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_coll_del_many.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_coll_dst.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_coll_find.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_coll_find1.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_coll_options.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_connect.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_init.py
                /usr/bin/python ./test/unit/mongo_class/repsetcoll_ins_doc.py
                /usr/bin/python ./test/unit/mongo_class/repset_connect.py
                /usr/bin/python ./test/unit/mongo_class/repset_init.py
                /usr/bin/python ./test/unit/mongo_class/rep_fetch_nodes.py
                /usr/bin/python ./test/unit/mongo_class/rep_init.py
                /usr/bin/python ./test/unit/mongo_class/server_adm_cmd.py
                /usr/bin/python ./test/unit/mongo_class/server_connect.py
                /usr/bin/python ./test/unit/mongo_class/server_disconnect.py
                /usr/bin/python ./test/unit/mongo_class/server_fetch_adr.py
                /usr/bin/python ./test/unit/mongo_class/server_fetch_dbs.py
                /usr/bin/python ./test/unit/mongo_class/server_fetch_svr_info.py
                /usr/bin/python ./test/unit/mongo_class/server_get_server_attr.py
                /usr/bin/python ./test/unit/mongo_class/server_init.py
                /usr/bin/python ./test/unit/mongo_class/server_is_locked.py
                /usr/bin/python ./test/unit/mongo_class/server_is_primary.py
                /usr/bin/python ./test/unit/mongo_class/server_lock_db.py
                /usr/bin/python ./test/unit/mongo_class/server_set_pass_config.py
                /usr/bin/python ./test/unit/mongo_class/server_set_ssl_config.py
                /usr/bin/python ./test/unit/mongo_class/server_unlock_db.py
                /usr/bin/python ./test/unit/mongo_class/server_upd_server_attr.py
                /usr/bin/python ./test/unit/mongo_class/server_upd_srv_stat.py
                /usr/bin/python ./test/unit/mongo_class/slaverep_connect.py
                /usr/bin/python ./test/unit/mongo_class/slaverep_init.py
                /usr/bin/python ./test/unit/mongo_libs/add_ssl_cmd.py
                /usr/bin/python ./test/unit/mongo_libs/create_cmd.py
                /usr/bin/python ./test/unit/mongo_libs/create_instance.py
                /usr/bin/python ./test/unit/mongo_libs/crt_base_cmd.py
                /usr/bin/python ./test/unit/mongo_libs/crt_coll_inst.py
                /usr/bin/python ./test/unit/mongo_libs/disconnect.py
                /usr/bin/python ./test/unit/mongo_libs/ins_doc.py
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
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/mongo-lib/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
